import fs from 'node:fs/promises';

const wasmBytes = await fs.readFile('./tfw_no_stack_locals_bg.wasm');
const { instance } = await WebAssembly.instantiate(wasmBytes, {
  wbg: {
    __wbindgen_init_externref_table() {},
    wbindgen_init_externref_table() {},
  },
});

const exp = instance.exports;
const mem = exp.memory;
const U8 = () => new Uint8Array(mem.buffer);
const TD = new TextDecoder();

console.log('[*] Exports:', Object.keys(exp));

const malloc = (n, align = 1) => exp.__wbindgen_malloc(n, align) >>> 0;
const check_flag = (ptr, len) => exp.check_flag(ptr, len) !== 0;

function checkBytes(bytes) {
  const ptr = malloc(bytes.length, 1);
  U8().set(bytes, ptr);
  return check_flag(ptr, bytes.length);
}

const targetQ = [
  3584201232957687288n,
  2570840801305670777n,
  -8682618338371224816n,
  -8684071750392024005n,
  -1955905064672638357n,
  6315395457821302550n,
  143009642011427521n,
];
function le64(q) {
  let x = BigInt(q);
  if (x < 0n) x = (1n << 64n) + x;
  const out = new Uint8Array(8);
  for (let i = 0; i < 8; i++) out[i] = Number((x >> BigInt(8 * i)) & 0xffn);
  return out;
}
const TARGET = (() => {
  const out = new Uint8Array(56);
  let o = 0;
  for (const q of targetQ) { out.set(le64(q), o); o += 8; }
  return out;
})();

const hex = a => Array.from(a).map(b => b.toString(16).padStart(2, '0')).join('');
const ZLEN = 56;

checkBytes(new Uint8Array(ZLEN));

const buf = U8();
const N = buf.length;

const windowStart = Math.max(0, N - 256 * 1024);
const windowEnd = N - ZLEN;

const PREFIXES = ['watctf{'];
const isPrintable = b => b === 10 || (b >= 32 && b <= 126);

function tryWindow(off) {
  // Candidate flag = TARGET ^ K
  const flag = new Uint8Array(ZLEN);
  for (let j = 0; j < ZLEN; j++) flag[j] = TARGET[j] ^ buf[off + j];

  const s = TD.decode(flag);
  if (!PREFIXES.some(p => s.startsWith(p))) return null;
  if (!s.includes('}')) return null;
  let printable = 0;
  for (const b of flag) if (isPrintable(b)) printable++;
  if (printable / ZLEN < 0.85) return null;

  return checkBytes(flag) ? { flag, s } : null;
}

let found = null;
let where = -1;
for (let i = windowStart; i <= windowEnd; i += 16) {
  const res = tryWindow(i);
  if (res) { found = res; where = i; break; }
}

if (!found) {
  for (let i = windowStart; i <= windowEnd; i++) {
    const res = tryWindow(i);
    if (res) { found = res; where = i; break; }
  }
}

if (!found) {
  console.log('[!] Keystream not found in recent window. Expanding scan…');
  for (let i = 0; i <= windowEnd; i += 16) {
    const res = tryWindow(i);
    if (res) { found = res; where = i; break; }
  }
  if (!found) {
    for (let i = 0; i <= windowEnd; i++) {
      const res = tryWindow(i);
      if (res) { found = res; where = i; break; }
    }
  }
}

console.log(`[+] Keystream window @ 0x${where.toString(16)}`);
console.log('[+] FLAG (utf8):', found.s);
console.log('[+] FLAG (hex):', hex(found.flag));
