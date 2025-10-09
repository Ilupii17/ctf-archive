export memory memory(initial: 17, max: 0);

global g_a:int = 1048576;

table T_a:funcref(min: 22, max: 22);
export table wbindgen_export_0:externref(min: 128, max: 0);

data d_calledResultunwraponanErrval(offset: 1048584) =
  "\01\00\00\00\01\00\00\00called `Result::unwrap()` on an `Err` value/ho"
  "me/hexular/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/cipher"
  "-0.4.4/src/stream.rs;\00\10\00]\00\00\00x\00\00\00'\00\00\00StreamCiph"
  "erError/build/rustc-1.87.0-src/library/alloc/src/slice.rs\00\b9\00\10\00"
  "2\00\00\00\be\01\00\00\1d\00\00\00OOOOHMYFAVOURITE/home/hexular/.cargo"
  "/registry/src/index.crates.io-1949cf8c6b5b557f/aes-0.8.4/src/soft/fixs"
  "lice32.rs\00\0c\01\10\00c\00\00\00\89\04\00\00\12\00\00\00\0c\01\10\00"
  "c\00\00\00\89\04\00\00=\00\00\00\0c\01\10\00c\00\00\00\14\05\00\00"\00"
  "\00\00\0c\01\10\00c\00\00\00\14\05\00\00\09\00\00\00Lazy instance has "
  "previously been poisoned\00\00\b0\01\10\00*\00\00\00/home/hexular/.car"
  "go/registry/src/index.crates.io-1949cf8c6b5b557f/once_cell-1.21.3/src/"
  "lib.rs\00\00\e4\01\10\00^\00\00\00\08\03\00\00\19\00\00\00reentrant in"
  "it\00\00T\02\10\00\0e\00\00\00\e4\01\10\00^\00\00\00z\02\00\00\0d\00\00"
  "\00/home/hexular/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/"
  "wasm-bindgen-0.2.101/src/convert/slices.rs\00\00\00|\02\10\00m\00\00\00"
  "\e8\00\00\00\01\00\00\00memory allocation of  bytes failed\00\00\fc\02"
  "\10\00\15\00\00\00\11\03\10\00\0d\00\00\00library/std/src/alloc.rs0\03"
  "\10\00\18\00\00\00d\01\00\00\09\00\00\00/build/rustc-1.87.0-src/librar"
  "y/alloc/src/raw_vec/mod.rsX\03\10\008\00\00\00.\02\00\00\11\00\00\00/b"
  "uild/rustc-1.87.0-src/library/alloc/src/string.rs\00\a0\03\10\003\00\00"
  "\00}\05\00\00\1b\00\00\00\05\00\00\00\0c\00\00\00\04\00\00\00\06\00\00"
  "\00\07\00\00\00\08\00\00\00\05\00\00\00\0c\00\00\00\04\00\00\00\09\00\00"
  "\00\00\00\00\00\08\00\00\00\04\00\00\00\0a\00\00\00/build/rustc-1.87.0"
  "-src/vendor/dlmalloc-0.2.7/src/dlmalloc.rsassertion failed: psize >= s"
  "ize + min_overhead\00\1c\04\10\00=\00\00\00\a8\04\00\00\09\00\00\00ass"
  "ertion failed: psize <= size + max_overhead\00\00\1c\04\10\00=\00\00\00"
  "\ae\04\00\00\0d\00\00\00\00\00\00\00\08\00\00\00\04\00\00\00\0a\00\00\00"
  "\00\00\00\00\08\00\00\00\04\00\00\00\0b\00\00\00\0c\00\00\00\0d\00\00\00"
  "\0e\00\00\00\0f\00\00\00\10\00\00\00\04\00\00\00\10\00\00\00\11\00\00\00"
  "\12\00\00\00\13\00\00\00capacity overflow\00\00\00 \05\10\00\11\00\00\00"
  "0001020304050607080910111213141516171819202122232425262728293031323334"
  "3536373839404142434445464748495051525354555657585960616263646566676869"
  "707172737475767778798081828384858687888990919293949596979899index out "
  "of bounds: the len is  but the index is \00\00\04\06\10\00 \00\00\00$\06"
  "\10\00\12\00\00\00: \00\00\01\00\00\00\00\00\00\00H\06\10\00\02";
data d_b(offset: 1050228) = "\02";

import function wbg_wbindgen_init_externref_table();

function f_b(a:int_ptr):int {
  var g:int_ptr;
  var b:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int }
  var c:int_ptr;
  var d:int_ptr;
  var e:int;
  var f:int;
  var h:int_ptr;
  var i:int;
  var k:int;
  var j:int_ptr = g_a - 16;
  g_a = j;
  if (a >= 245) {
    if (a > -65588) goto B_a;
    c = a + 11;
    f = c & -8;
    i = 1050688[0]:int;
    if (eqz(i)) goto B_d;
    h = 31;
    if (a <= 16777204) { h = (f >> 6 - (a = clz(c >> 8)) & 1) - (a << 1) + 62 }
    a = 0 - f;
    c = ((h << 2) + 1050276)[0]:int;
    if (eqz(c)) goto B_g;
    e = f << select_if(25 - (h >> 1), 0, h != 31);
    loop L_j {
      g = c[1] & -8;
      if (g < f) goto B_k;
      g = g - f;
      if (g >= a) goto B_k;
      d = c;
      a = g;
      if (a) goto B_k;
      a = 0;
      b = c;
      goto B_f;
      label B_k:
      g = c[5];
      b = 
        select_if(select_if(g, b, g != (c = (c + (e >> 29 & 4))[4]:int)), b, g);
      e = e << 1;
      if (c) continue L_j;
    }
    goto B_g;
  }
  c = 1050684[0]:int;
  b = c >> (a = (f = select_if(16, a + 11 & 504, a < 11)) >> 3);
  if (b & 3) {
    g = ((b ^ -1) & 1) + a;
    b = g << 3;
    a = b + 1050276;
    d = a + 144;
    if (d != (e = (a = a[38])[2])) {
      e[3]:int = d;
      d[2] = e;
      goto B_m;
    }
    1050684[0]:int = c & -2 << g;
    label B_m:
    d = a + 8;
    a[1] = b | 3;
    a = a + b;
    a[1] = a[1] | 1;
    goto B_a;
  }
  if (f <= 1050692[0]:int) goto B_d;
  if (eqz(b)) {
    a = 1050688[0]:int;
    if (eqz(a)) goto B_d;
    d = ((ctz(a) << 2) + 1050276)[0]:int;
    a = (d[1] & -8) - f;
    c = d;
    loop L_r {
      b = d[4];
      if (b) goto B_s;
      b = d[5];
      if (b) goto B_s;
      h = c[6];
      if (c == (b = c[3])) {
        d = (c + select_if(20, 16, b = c[5]))[0]:int;
        if (d) goto B_u;
        b = 0;
        goto B_t;
      }
      d = c[2];
      d[3] = b;
      b.c = d;
      goto B_t;
      label B_u:
      e = select_if(c + 20, c + 16, b);
      loop L_w {
        g = e;
        b = d;
        e = select_if(b + 20, b + 16, d = b.f);
        d = (b + select_if(20, 16, d))[0]:int;
        if (d) continue L_w;
      }
      g[0] = 0;
      label B_t:
      if (eqz(h)) goto B_o;
      d = c[7];
      e = (d << 2) + 1050276;
      if (e[0]:int != c) {
        if (c != h[4]) {
          h[5] = b;
          if (b) goto B_x;
          goto B_o;
        }
        h[4] = b;
        if (b) goto B_x;
        goto B_o;
      }
      e[0]:int = b;
      if (eqz(b)) goto B_p;
      label B_x:
      b.g = h;
      d = c[4];
      if (d) {
        b.e = d;
        d[6] = b;
      }
      d = c[5];
      if (eqz(d)) goto B_o;
      b.f = d;
      d[6] = b;
      goto B_o;
      label B_s:
      d = (b.b & -8) - f;
      a = select_if(d, a, d = a > d);
      c = select_if(b, c, d);
      d = b;
      continue L_r;
    }
    unreachable;
  }
  d = 2 << a;
  g = ctz((d | 0 - d) & b << a);
  d = g << 3;
  b = d + 1050420;
  if (b != (e = (a = b.c)[2])) {
    e[3]:int = b;
    b.c = e;
    goto B_ba;
  }
  1050684[0]:int = c & -2 << g;
  label B_ba:
  a[1] = f | 3;
  g = a + f;
  g[1] = (e = d - f) | 1;
  (a + d)[0]:int = e;
  d = 1050692[0]:int;
  if (d) {
    b = (d & -8) + 1050420;
    c = 1050700[0]:int;
    d = {
          f = 1050684[0]:int;
          if (eqz(f & (d = 1 << (d >> 3)))) {
            1050684[0]:int = d | f;
            b;
            goto B_ea;
          }
          b.c;
          label B_ea:
        }
    b.c = c;
    d[3] = c;
    c[3] = b;
    c[2] = d;
  }
  d = a + 8;
  1050700[0]:int = g;
  1050692[0]:int = e;
  goto B_a;
  label B_p:
  1050688[0]:int = 1050688[0]:int & -2 << d;
  label B_o:
  if (a >= 16) {
    c[1] = f | 3;
    e = c + f;
    e[1]:int = a | 1;
    (a + e)[0]:int = a;
    g = 1050692[0]:int;
    if (eqz(g)) goto B_ha;
    b = (g & -8) + 1050420;
    d = 1050700[0]:int;
    g = {
          f = 1050684[0]:int;
          if (eqz(f & (g = 1 << (g >> 3)))) {
            1050684[0]:int = f | g;
            b;
            goto B_ja;
          }
          b.c;
          label B_ja:
        }
    b.c = d;
    g[3] = d;
    d[3] = b;
    d[2] = g;
    goto B_ha;
  }
  c[1] = (a = a + f) | 3;
  a = a + c;
  a[1] = a[1] | 1;
  goto B_ga;
  label B_ha:
  1050700[0]:int = e;
  1050692[0]:int = a;
  label B_ga:
  d = c + 8;
  goto B_a;
  label B_g:
  if (eqz(b | d)) {
    d = 0;
    b = 2 << h;
    b = (b | 0 - b) & i;
    if (eqz(b)) goto B_d;
    b = ((ctz(b) << 2) + 1050276)[0]:int;
  }
  if (eqz(b)) goto B_e;
  label B_f:
  loop L_ma {
    i = select_if(b, d, h = (g = (e = b.b & -8) - f) < a);
    c = b.e;
    if (eqz(c)) { c = b.f }
    d = select_if(d, i, b = e < f);
    a = select_if(a, select_if(g, a, h), b);
    b = c;
    if (b) continue L_ma;
  }
  label B_e:
  if (eqz(d)) goto B_d;
  if (f <= (b = 1050692[0]:int) & a >= b - f) goto B_d;
  h = d[6];
  if (d == (b = d[3])) {
    c = (d + select_if(20, 16, b = d[5]))[0]:int;
    if (c) goto B_pa;
    b = 0;
    goto B_oa;
  }
  c = d[2];
  c[3] = b;
  b.c = c;
  goto B_oa;
  label B_pa:
  e = select_if(d + 20, d + 16, b);
  loop L_ra {
    g = e;
    b = c;
    e = select_if(b + 20, b + 16, c = b.f);
    c = (b + select_if(20, 16, c))[0]:int;
    if (c) continue L_ra;
  }
  g[0] = 0;
  label B_oa:
  if (eqz(h)) goto B_b;
  c = d[7];
  e = (c << 2) + 1050276;
  if (e[0]:int != d) {
    if (d != h[4]) {
      h[5] = b;
      if (b) goto B_sa;
      goto B_b;
    }
    h[4] = b;
    if (b) goto B_sa;
    goto B_b;
  }
  e[0]:int = b;
  if (eqz(b)) goto B_c;
  label B_sa:
  b.g = h;
  c = d[4];
  if (c) {
    b.e = c;
    c[6] = b;
  }
  c = d[5];
  if (eqz(c)) goto B_b;
  b.f = c;
  c[6] = b;
  goto B_b;
  label B_d:
  if (f > (b = 1050692[0]:int)) {
    if (f >= (a = 1050696[0]:int)) {
      c = f + 65583 & -65536;
      a = memory_grow(c >> 16);
      b = j + 4;
      b.c = 0;
      b.b = select_if(0, c & -65536, c = a == -1);
      b.a = select_if(0, a << 16, c);
      d = 0;
      a = j[1];
      if (eqz(a)) goto B_a;
      h = j[3];
      1050708[0]:int = (b = (g = j[2]) + 1050708[0]:int);
      1050712[0]:int = select_if(b, c = 1050712[0]:int, b > c);
      c = 1050704[0]:int;
      if (eqz(c)) {
        b = 1050720[0]:int;
        if (eqz(select_if(b, 0, a >= b))) { 1050720[0]:int = a }
        1050724[0]:int = 4095;
        1050416[0]:int = h;
        1050408[0]:int = g;
        1050404[0]:int = a;
        1050432[0]:int = 1050420;
        1050440[0]:int = 1050428;
        1050428[0]:int = 1050420;
        1050448[0]:int = 1050436;
        1050436[0]:int = 1050428;
        1050456[0]:int = 1050444;
        1050444[0]:int = 1050436;
        1050464[0]:int = 1050452;
        1050452[0]:int = 1050444;
        1050472[0]:int = 1050460;
        1050460[0]:int = 1050452;
        1050480[0]:int = 1050468;
        1050468[0]:int = 1050460;
        1050488[0]:int = 1050476;
        1050476[0]:int = 1050468;
        1050496[0]:int = 1050484;
        1050484[0]:int = 1050476;
        1050492[0]:int = 1050484;
        1050504[0]:int = 1050492;
        1050500[0]:int = 1050492;
        1050512[0]:int = 1050500;
        1050508[0]:int = 1050500;
        1050520[0]:int = 1050508;
        1050516[0]:int = 1050508;
        1050528[0]:int = 1050516;
        1050524[0]:int = 1050516;
        1050536[0]:int = 1050524;
        1050532[0]:int = 1050524;
        1050544[0]:int = 1050532;
        1050540[0]:int = 1050532;
        1050552[0]:int = 1050540;
        1050548[0]:int = 1050540;
        1050560[0]:int = 1050548;
        1050568[0]:int = 1050556;
        1050556[0]:int = 1050548;
        1050576[0]:int = 1050564;
        1050564[0]:int = 1050556;
        1050584[0]:int = 1050572;
        1050572[0]:int = 1050564;
        1050592[0]:int = 1050580;
        1050580[0]:int = 1050572;
        1050600[0]:int = 1050588;
        1050588[0]:int = 1050580;
        1050608[0]:int = 1050596;
        1050596[0]:int = 1050588;
        1050616[0]:int = 1050604;
        1050604[0]:int = 1050596;
        1050624[0]:int = 1050612;
        1050612[0]:int = 1050604;
        1050632[0]:int = 1050620;
        1050620[0]:int = 1050612;
        1050640[0]:int = 1050628;
        1050628[0]:int = 1050620;
        1050648[0]:int = 1050636;
        1050636[0]:int = 1050628;
        1050656[0]:int = 1050644;
        1050644[0]:int = 1050636;
        1050664[0]:int = 1050652;
        1050652[0]:int = 1050644;
        1050672[0]:int = 1050660;
        1050660[0]:int = 1050652;
        1050680[0]:int = 1050668;
        1050668[0]:int = 1050660;
        1050676[0]:int = 1050668;
        1050704[0]:int = (c = (b = a + 15 & -8) - 8);
        c[1] = (b = (c = g - 40) + a - b + 8) | 1;
        1050696[0]:int = b;
        (a + c)[1]:int = 40;
        1050716[0]:int = 2097152;
        goto B_wa;
      }
      b = 1050404;
      loop L_gb {
        e = b.a;
        if (e + (i = b.b) != a) {
          b = b.c;
          if (b) continue L_gb;
          goto B_fb;
        }
      }
      if (c < e | a <= c) goto B_fb;
      e = b.d;
      if (e & 1) goto B_fb;
      if (e >> 1 == h) goto B_ab;
      label B_fb:
      1050720[0]:int = select_if(b = 1050720[0]:int, a, a > b);
      e = a + g;
      b = 1050404;
      loop L_kb {
        if (e != (i = b.a)) {
          b = b.c;
          if (b) continue L_kb;
          goto B_jb;
        }
      }
      e = b.d;
      if (e & 1) goto B_jb;
      if (e >> 1 == h) goto B_ib;
      label B_jb:
      b = 1050404;
      loop L_mb {
        if (c >= (e = b.a)) { if (c < (i = e + b.b)) goto B_nb }
        b = b.c;
        continue L_mb;
        label B_nb:
      }
      b = a + 15 & -8;
      e = b - 8;
      e[1]:int = (b = (k = g - 40) + a - b + 8) | 1;
      1050716[0]:int = 2097152;
      1050704[0]:int = e;
      1050696[0]:int = b;
      (a + k)[1]:int = 40;
      e = select_if(c, b = (i - 32 & -8) - 8, b < c + 16);
      e[1]:int = 27;
      var l:long = 1050404[0]:long@4;
      (e + 16)[0]:long@4 = 1050412[0]:long@4;
      e[2]:long@4 = l;
      1050416[0]:int = h;
      1050408[0]:int = g;
      1050404[0]:int = a;
      1050412[0]:int = e + 8;
      b = e + 28;
      loop L_pb {
        b.a = 7;
        b = b + 4;
        if (b < i) continue L_pb;
      }
      if (c == e) goto B_wa;
      e[1]:int = e[1]:int & -2;
      c[1] = (a = e - c) | 1;
      e[0]:int = a;
      if (a >= 256) {
        f_l(c, a);
        goto B_wa;
      }
      b = (a & 248) + 1050420;
      a = {
            e = 1050684[0]:int;
            if (eqz(e & (a = 1 << (a >> 3)))) {
              1050684[0]:int = a | e;
              b;
              goto B_rb;
            }
            b.c;
            label B_rb:
          }
      b.c = c;
      a[3] = c;
      c[3] = b;
      c[2] = a;
      goto B_wa;
      label B_ib:
      b.a = a;
      b.b = b.b + g;
      d = (a + 15 & -8) - 8;
      d[1] = f | 3;
      a = (i + 15 & -8) - 8;
      f = a - (b = d + f);
      if (a == 1050704[0]:int) goto B_za;
      if (a == 1050700[0]:int) goto B_ya;
      c = a[1];
      if ((c & 3) == 1) {
        f_j(a, c = c & -8);
        f = c + f;
        a = a + c;
        c = a[1];
      }
      a[1] = c & -2;
      b.b = f | 1;
      (b + f)[0]:int = f;
      if (f >= 256) {
        f_l(b, f);
        goto B_xa;
      }
      a = (f & 248) + 1050420;
      c = {
            c = 1050684[0]:int;
            if (eqz(c & (e = 1 << (f >> 3)))) {
              1050684[0]:int = c | e;
              a;
              goto B_vb;
            }
            a[2];
            label B_vb:
          }
      a[2] = b;
      c[3] = b;
      b.d = a;
      b.c = c;
      goto B_xa;
    }
    1050696[0]:int = (b = a - f);
    1050704[0]:int = (c = (a = 1050704[0]:int) + f);
    c[1] = b | 1;
    a[1] = f | 3;
    d = a + 8;
    goto B_a;
  }
  a = 1050700[0]:int;
  c = b - f;
  if (c <= 15) {
    1050700[0]:int = 0;
    1050692[0]:int = 0;
    a[1] = b | 3;
    b = a + b;
    b.b = b.b | 1;
    goto B_xb;
  }
  1050692[0]:int = c;
  1050700[0]:int = (d = a + f);
  d[1] = c | 1;
  (a + b)[0]:int = c;
  a[1] = f | 3;
  label B_xb:
  d = a + 8;
  goto B_a;
  label B_ab:
  b.b = g + i;
  a = 1050704[0]:int;
  b = a + 15 & -8;
  c = b - 8;
  c[1] = (b = (e = 1050696[0]:int + g) + a - b + 8) | 1;
  1050716[0]:int = 2097152;
  1050704[0]:int = c;
  1050696[0]:int = b;
  (a + e)[1]:int = 40;
  goto B_wa;
  label B_za:
  1050704[0]:int = b;
  1050696[0]:int = (a = 1050696[0]:int + f);
  b.b = a | 1;
  goto B_xa;
  label B_ya:
  b.b = (a = 1050692[0]:int + f) | 1;
  1050700[0]:int = b;
  1050692[0]:int = a;
  (a + b)[0]:int = a;
  label B_xa:
  d = d + 8;
  goto B_a;
  label B_wa:
  a = 1050696[0]:int;
  if (a <= f) goto B_a;
  1050696[0]:int = (b = a - f);
  1050704[0]:int = (c = (a = 1050704[0]:int) + f);
  c[1] = b | 1;
  a[1] = f | 3;
  d = a + 8;
  goto B_a;
  label B_c:
  1050688[0]:int = 1050688[0]:int & -2 << c;
  label B_b:
  if (a >= 16) {
    d[1] = f | 3;
    b = d + f;
    b.b = a | 1;
    (a + b)[0]:int = a;
    if (a >= 256) {
      f_l(b, a);
      goto B_zb;
    }
    c = (a & 248) + 1050420;
    a = {
          e = 1050684[0]:int;
          if (eqz(e & (a = 1 << (a >> 3)))) {
            1050684[0]:int = a | e;
            c;
            goto B_cc;
          }
          c[2];
          label B_cc:
        }
    c[2] = b;
    a[3] = b;
    b.d = c;
    b.c = a;
    goto B_zb;
  }
  d[1] = (a = a + f) | 3;
  a = a + d;
  a[1] = a[1] | 1;
  label B_zb:
  d = d + 8;
  label B_a:
  g_a = j + 16;
  return d;
}

function f_c(a:{ a:int, b:int, c:int, d:int }) {
  var d:{ a:int, b:int }
  var e:int;
  var f:int_ptr;
  var b:int = a - 8;
  var c:{ a:int, b:int, c:int } = b + (a = (d = (a - 4)[0]:int) & -8);
  if (d & 1) goto B_b;
  if (eqz(d & 2)) goto B_a;
  d = b[0]:int;
  a = d + a;
  b = b - d;
  if (b == 1050700[0]:int) {
    d = c.b;
    if ((d & 3) != 3) goto B_b;
    c.b = d & -2;
    b[1]:int = a | 1;
    1050692[0]:int = a;
    c.a = a;
    return ;
  }
  f_j(b, d);
  label B_b:
  d = c.b;
  if (eqz(d & 2)) {
    if (c == 1050704[0]:int) goto B_j;
    if (c == 1050700[0]:int) goto B_i;
    f_j(c, c = d & -8);
    b[1]:int = (a = a + c) | 1;
    (a + b)[0]:int = a;
    if (b != 1050700[0]:int) goto B_k;
    1050692[0]:int = a;
    return ;
  }
  c.b = d & -2;
  b[1]:int = a | 1;
  (a + b)[0]:int = a;
  label B_k:
  if (a < 256) goto B_h;
  c = 31;
  b[4]:long@4 = 0L;
  if (a <= 16777215) { c = (a >> 6 - (c = clz(a >> 8)) & 1) - (c << 1) + 62 }
  b[7]:int = c;
  d = (c << 2) + 1050276;
  e = 1 << c;
  if (e & 1050688[0]:int) goto B_g;
  d.a = b;
  b[6]:int = d;
  1050688[0]:int = 1050688[0]:int | e;
  goto B_f;
  label B_j:
  1050704[0]:int = b;
  1050696[0]:int = (a = 1050696[0]:int + a);
  b[1]:int = a | 1;
  if (1050700[0]:int == b) {
    1050692[0]:int = 0;
    1050700[0]:int = 0;
  }
  if (a <= 1050716[0]:int) goto B_a;
  if (a < 41) goto B_d;
  a = 1050404;
  loop L_o {
    if (b >= (c = a.a)) { if (b < c + a.b) goto B_d }
    a = a.c;
    continue L_o;
  }
  unreachable;
  label B_i:
  b[1]:int = (a = 1050692[0]:int + a) | 1;
  1050700[0]:int = b;
  1050692[0]:int = a;
  (a + b)[0]:int = a;
  return ;
  label B_h:
  c = (a & 248) + 1050420;
  a = {
        d = 1050684[0]:int;
        if (eqz(d & (a = 1 << (a >> 3)))) {
          1050684[0]:int = a | d;
          c;
          goto B_q;
        }
        c.c;
        label B_q:
      }
  c.c = b;
  a.d = b;
  b[3]:int = c;
  b[2]:int = a;
  return ;
  label B_g:
  if (a == ((d = d.a).b & -8)) {
    c = d;
    goto B_t;
  }
  e = a << select_if(25 - (c >> 1), 0, c != 31);
  loop L_v {
    f = d + (e >> 29 & 4);
    c = f[4];
    if (eqz(c)) goto B_s;
    e = e << 1;
    d = c;
    if ((c.b & -8) != a) continue L_v;
  }
  label B_t:
  a = c.c;
  a.d = b;
  c.c = b;
  b[6]:int = 0;
  b[3]:int = c;
  b[2]:int = a;
  goto B_e;
  label B_s:
  (f + 16)[0]:int = b;
  b[6]:int = d;
  label B_f:
  b[3]:int = b;
  b[2]:int = b;
  label B_e:
  1050724[0]:int = (a = 1050724[0]:int - 1);
  if (a) goto B_a;
  a = 1050412[0]:int;
  if (eqz(a)) {
    b = 0;
    goto B_w;
  }
  b = 0;
  loop L_y {
    b = b + 1;
    a = a.c;
    if (a) continue L_y;
  }
  label B_w:
  1050724[0]:int = select_if(4095, b, b <= 4095);
  return ;
  label B_d:
  a = 1050412[0]:int;
  if (eqz(a)) {
    b = 0;
    goto B_z;
  }
  b = 0;
  loop L_ba {
    b = b + 1;
    a = a.c;
    if (a) continue L_ba;
  }
  label B_z:
  1050716[0]:int = -1;
  1050724[0]:int = select_if(4095, b, b <= 4095);
  label B_a:
}

function f_d(a:int, b:int_ptr) {
  var d:int_ptr;
  var f:int_ptr;
  var c:{ a:int, b:int, c:int } = a + b;
  d = a[1]:int;
  if (d & 1) goto B_c;
  if (eqz(d & 2)) goto B_b;
  d = a[0]:int;
  b = d + b;
  a = a - d;
  if (a == 1050700[0]:int) {
    d = c.b;
    if ((d & 3) != 3) goto B_c;
    c.b = d & -2;
    a[1]:int = b | 1;
    1050692[0]:int = b;
    c.a = b;
    goto B_b;
  }
  f_j(a, d);
  label B_c:
  d = c.b;
  if (eqz(d & 2)) {
    if (c == 1050704[0]:int) goto B_f;
    if (c == 1050700[0]:int) goto B_e;
    f_j(c, c = d & -8);
    a[1]:int = (b = b + c) | 1;
    (a + b)[0]:int = b;
    if (a != 1050700[0]:int) goto B_g;
    1050692[0]:int = b;
    return ;
  }
  c.b = d & -2;
  a[1]:int = b | 1;
  (a + b)[0]:int = b;
  label B_g:
  if (b >= 256) {
    var e:int = 31;
    a[4]:long@4 = 0L;
    if (b <= 16777215) { e = (b >> 6 - (c = clz(b >> 8)) & 1) - (c << 1) + 62 }
    a[7]:int = e;
    c = (e << 2) + 1050276;
    d = 1 << e;
    if (eqz(d & 1050688[0]:int)) {
      c.a = a;
      a[6]:int = c;
      1050688[0]:int = 1050688[0]:int | d;
      goto B_k;
    }
    if (b == ((d = c.a)[1] & -8)) {
      c = d;
      goto B_n;
    }
    e = b << select_if(25 - (e >> 1), 0, e != 31);
    loop L_p {
      f = d + (e >> 29 & 4);
      c = f[4];
      if (eqz(c)) goto B_m;
      e = e << 1;
      d = c;
      if ((c.b & -8) != b) continue L_p;
    }
    label B_n:
    b = c.c;
    b[3] = a;
    c.c = a;
    a[6]:int = 0;
    goto B_a;
    label B_m:
    (f + 16)[0]:int = a;
    a[6]:int = d;
    label B_k:
    a[3]:int = a;
    a[2]:int = a;
    return ;
  }
  c = (b & 248) + 1050420;
  b = {
        d = 1050684[0]:int;
        if (eqz(d & (b = 1 << (b >> 3)))) {
          1050684[0]:int = b | d;
          c;
          goto B_q;
        }
        c.c;
        label B_q:
      }
  c.c = a;
  b[3] = a;
  goto B_a;
  label B_f:
  1050704[0]:int = a;
  1050696[0]:int = (b = 1050696[0]:int + b);
  a[1]:int = b | 1;
  if (a != 1050700[0]:int) goto B_b;
  1050692[0]:int = 0;
  1050700[0]:int = 0;
  return ;
  label B_e:
  a[1]:int = (b = 1050692[0]:int + b) | 1;
  1050700[0]:int = a;
  1050692[0]:int = b;
  (a + b)[0]:int = b;
  label B_b:
  return ;
  label B_a:
  a[3]:int = c;
  a[2]:int = b;
}

function f_e(a:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int }) {
  var b:int;
  var e:int;
  var h:int;
  var f:int;
  var k:int;
  var m:int;
  var r:int;
  var i:int;
  var g:int;
  var l:int;
  var s:int;
  var j:int;
  var c:int;
  var d:int;
  var t:int;
  var n:int;
  var o:int;
  var x:int;
  var p:int;
  var q:int;
  var y:int;
  var z:int;
  var u:int;
  var v:int;
  var w:int;
  var aa:int;
  var ba:int;
  a.b =
    (ba = 
       ((u = 
           ((v = 
               (aa = 
                  (q = 
                     (w = 
                        ((v = 
                            ((l = 
                                (q = 
                                   ((((d = 
                                         (j = 
                                            (l = 
                                               (i = 
                                                  (r = (h = (b = a.h) ^ (e = a.b)) ^ (m = (f = a.e) ^ (k = a.c))) ^ a.d) ^
                                               (g = a.g)) ^
                                            (s = b ^ f)) ^
                                         (c = g ^ a.f)) ^
                                      ((t = e ^ (g = c ^ (e = a.a))) & g)) ^
                                     (n = d & h)) ^
                                    h) ^
                                   (p = (o = j & s) ^ ((x = (i = c ^ (c = i ^ k)) ^ j) & m))) &
                                (u = p ^ ((p = c & r) ^ (l ^ ((y = c ^ e) & (z = t ^ (k = b ^ k))))))) ^
                             (f = (o = (i & k) ^ o) ^ (p ^ ((((p = f ^ g) & e) ^ k) ^ i)))) &
                            ((b = o ^ ((n ^ (d ^ ((n = e ^ j) & (o = b ^ g)))) ^ b)) ^ q)) ^
                         l) &
                        b) ^
                     q) &
                  c) ^
               (e & (e = b ^ v))) ^
            ((b = f ^ ((c = b ^ l) & (f = f ^ u))) & n)) ^
           (n = d & (l = (d = ((c ^ w) & b) ^ f) ^ b))) ^
        (d & t)) ^
       (w = (m & (t = (f = d ^ (c = e ^ q)) ^ (m = b ^ e))) ^ (s = m & s))) ^
    (i = (d = (g = n ^ (d & g)) ^ (t & x)) ^ ((h = h & l) ^ ((f & i) ^ v)));
  a.a = h ^ ba;
  a.h = (r = (h = w ^ (c & z)) ^ (q & r)) ^ (j = d ^ (j & m));
  a.f = (d = i ^ (b & o)) ^ (((f & k) ^ s) ^ j);
  a.e = (b = (((c & y) ^ aa) ^ g) ^ r);
  a.c = (h ^ (e & p)) ^ d;
  a.g = b ^ j;
  a.d = b ^ u;
}

function f_f(a:{ a:int, b:int }, b:int, c:{ a:int, b:int, c:int, d:int, e:int, f:int }):int {
  var f:int;
  var j:int;
  var e:int;
  var g:int;
  var d:int = g_a - 16;
  g_a = d;
  d[1]:int = b;
  d[0]:int = a;
  d[2]:long@4 = 3758096416L;
  let t0 = 
    {
      j = c.e;
      if (j) {
        a = c.f;
        if (a) goto B_d;
        goto B_c;
      }
      a = c.d;
      if (eqz(a)) goto B_c;
      b = c.c;
      e = b + (a << 3);
      g = (a - 1 & 536870911) + 1;
      a = c.a;
      loop L_f {
        f = (a + 4)[0]:int;
        if (eqz(f)) goto B_g;
        if (eqz(call_indirect(d[0]:int, a.a, f, (d[1]:int)[3]:int))) goto B_g;
        1;
        goto B_a;
        label B_g:
        1;
        if (call_indirect(b[0]:int, d, (b + 4)[0]:int)) goto B_a;
        a = a + 8;
        if (e != (b = b + 8)) continue L_f;
      }
      goto B_b;
      label B_d:
      var k:int = a * 24;
      g = (a - 1 & 536870911) + 1;
      e = c.c;
      a = c.a;
      loop L_h {
        b = (a + 4)[0]:int;
        if (eqz(b)) goto B_i;
        if (eqz(call_indirect(d[0]:int, a.a, b, (d[1]:int)[3]:int))) goto B_i;
        1;
        goto B_a;
        label B_i:
        var h:int = 0;
        var i:int = 0;
        b = f + j;
        br_table[B_k, B_j, ..B_l]((b + 8)[0]:ushort - 1);
        label B_l:
        i = (b + 10)[0]:ushort;
        goto B_j;
        label B_k:
        i = (e + ((b + 12)[0]:int << 3))[2]:ushort;
        label B_j:
        br_table[B_n, B_m, ..B_o](b[0]:ushort - 1)
        label B_o:
        h = (b + 2)[0]:ushort;
        goto B_m;
        label B_n:
        h = (e + ((b + 4)[0]:int << 3))[2]:ushort;
        label B_m:
        d[7]:short = h;
        d[6]:short = i;
        d[2]:int = (b + 20)[0]:int;
        1;
        if (
          call_indirect((b = e + ((b + 16)[0]:int << 3))[0]:int, d, (b + 4)[0]:int)) goto B_a;
        a = a + 8;
        f = f + 24;
        if (f != k) continue L_h;
      }
      goto B_b;
      label B_c:
      label B_b:
      if (g >= c.b) goto B_p;
      if (
        eqz(
          call_indirect(d[0]:int, (a = c.a + (g << 3)).a, a.b, (d[1]:int)[3]:int))) goto B_p;
      1;
      goto B_a;
      label B_p:
      0;
      label B_a:
    }
  g_a = d + 16;
  return t0;
}

function f_g(a:int_ptr@1, b:int, c:int) {
  var g:int;
  var e:int_ptr;
  var f:int;
  var h:int;
  var k:int;
  var l:int;
  var i:int;
  var o:int;
  var j:int_ptr;
  var d:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int } = 
    g_a - 32;
  g_a = d;
  f_h(d, c, c + 16);
  c = 0;
  loop L_a {
    j = c + d;
    j[0] = j[0] ^ (b + c)[0]:int;
    c = c + 4;
    if (c != 32) continue L_a;
  }
  j = b + 128;
  var m:int = b + 32;
  var n:int = b + 96;
  var p:int = b - -64;
  var q:int = 8;
  loop L_b {
    f_e(d);
    d.h =
      ((e = 
          (g = ((c = d.g) << 22 & 1061109567) | (c << 30 & -1061109568)) ^ c) ^
       (((c = 
            (f = ((c = d.h) << 22 & 1061109567) | (c << 30 & -1061109568)) ^ c) <<
         12 &
         252645135) |
        (c << 20 & -252645136))) ^
      f;
    d.g =
      g ^
      ((f = 
          (h = ((f = d.f) << 22 & 1061109567) | (f << 30 & -1061109568)) ^ f) ^
       ((e << 12 & 252645135) | (e << 20 & -252645136)));
    d.f =
      ((e = 
          (k = ((e = d.e) << 22 & 1061109567) | (e << 30 & -1061109568)) ^ e) ^
       ((f << 12 & 252645135) | (f << 20 & -252645136))) ^
      h;
    d.c =
      ((f = 
          (l = ((f = d.b) << 22 & 1061109567) | (f << 30 & -1061109568)) ^ f) ^
       (((g = 
            (h = ((g = d.c) << 22 & 1061109567) | (g << 30 & -1061109568)) ^ g) <<
         12 &
         252645135) |
        (g << 20 & -252645136))) ^
      h;
    d.a =
      ((((h = 
            (i = ((h = d.a) << 22 & 1061109567) | (h << 30 & -1061109568)) ^ h) <<
         12 &
         252645135) |
        (h << 20 & -252645136)) ^
       i) ^
      c;
    d.e =
      (k ^
       ((i = 
           (o = ((i = d.d) << 22 & 1061109567) | (i << 30 & -1061109568)) ^ i) ^
        ((e << 12 & 252645135) | (e << 20 & -252645136)))) ^
      c;
    d.d =
      ((g ^ ((i << 12 & 252645135) | (i << 20 & -252645136))) ^ o) ^ c;
    d.b =
      ((h ^ ((f << 12 & 252645135) | (f << 20 & -252645136))) ^ l) ^ c;
    c = 0;
    loop L_c {
      e = c + d;
      e[0] = e[0] ^ (c + m)[0]:int;
      c = c + 4;
      if (c != 32) continue L_c;
    }
    if (q == 72) {
      c = 0;
      loop L_e {
        j = c + d;
        j[0] = ((j = j[0]) ^ (j = (j ^ j >> 4) & 251662080) << 4) ^ j;
        c = c + 4;
        if (c != 32) continue L_e;
      }
      b = b + 320;
      f_e(d);
      c = 0;
      loop L_f {
        j = c + d;
        j[0] = j[0] ^ (b + c)[0]:int;
        c = c + 4;
        if (c != 32) continue L_f;
      }
      a[28] =
        (o = 
           ((b = 
               (q = 
                  ((b = (j = ((b = d.h) ^ (c = d.g) >> 1) & 1431655765) ^ b) ^
                   (m = (p = ((m = d.f) ^ (n = d.e) >> 1) & 1431655765) ^ m) >> 2) &
                  858993459) ^
               b) ^
            (e = 
               (l = 
                  ((e = (g = ((e = d.d) ^ (f = d.c) >> 1) & 1431655765) ^ e) ^
                   (h = (k = ((h = d.b) ^ (i = d.a) >> 1) & 1431655765) ^ h) >> 2) &
                  858993459) ^
               e) >>
            4) &
           252645135) ^
        b;
      a[24] =
        (q = ((b = q << 2 ^ m) ^ (m = l << 2 ^ h) >> 4) & 252645135) ^ b;
      a[20] = o << 4 ^ e;
      a[12] =
        (f = 
           ((b = (j = ((b = c ^ j << 1) ^ (c = n ^ p << 1) >> 2) & 858993459) ^ b) ^
            (n = (e = ((n = f ^ g << 1) ^ (p = i ^ k << 1) >> 2) & 858993459) ^ n) >>
            4) &
           252645135) ^
        b;
      a[16] = q << 4 ^ m;
      a[8] =
        (j = ((b = j << 2 ^ c) ^ (c = e << 2 ^ p) >> 4) & 252645135) ^ b;
      a[4] = f << 4 ^ n;
      a[0] = j << 4 ^ c;
      g_a = d + 32;
    } else {
      f_e(d);
      d.h =
        ((g = (f = ((c = d.g) << 20 & 252645135) | (c << 28 & -252645136)) ^ c) ^
         (c = (e = ((c = d.h) << 20 & 252645135) | (c << 28 & -252645136)) ^ c) <<
         16) ^
        e;
      d.g =
        f ^
        ((i = (h = ((e = d.f) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) ^
         g << 16);
      d.f =
        h ^
        ((g = (f = ((e = d.e) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) ^
         i << 16);
      d.c =
        ((i = (h = ((e = d.b) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) ^
         (l = (k = ((e = d.c) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) <<
         16) ^
        k;
      d.a =
        ((o = (k = ((e = d.a) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) <<
         16 ^
         k) ^
        c;
      d.e =
        (f ^
         ((e = (k = ((e = d.d) << 20 & 252645135) | (e << 28 & -252645136)) ^ e) ^
          g << 16)) ^
        c;
      d.d = ((l ^ e << 16) ^ k) ^ c;
      d.b = ((o ^ i << 16) ^ h) ^ c;
      c = 0;
      loop L_g {
        e = c + d;
        e[0] = e[0] ^ (c + p)[0]:int;
        c = c + 4;
        if (c != 32) continue L_g;
      }
      f_e(d);
      d.h =
        ((e = (g = ((c = d.g) << 18 & 50529027) | (c << 26 & -50529028)) ^ c) ^
         (((c = (f = ((c = d.h) << 18 & 50529027) | (c << 26 & -50529028)) ^ c) <<
           12 &
           252645135) |
          (c << 20 & -252645136))) ^
        f;
      d.g =
        g ^
        ((f = (h = ((f = d.f) << 18 & 50529027) | (f << 26 & -50529028)) ^ f) ^
         ((e << 12 & 252645135) | (e << 20 & -252645136)));
      d.f =
        ((e = (k = ((e = d.e) << 18 & 50529027) | (e << 26 & -50529028)) ^ e) ^
         ((f << 12 & 252645135) | (f << 20 & -252645136))) ^
        h;
      d.c =
        ((f = (l = ((f = d.b) << 18 & 50529027) | (f << 26 & -50529028)) ^ f) ^
         (((g = (h = ((g = d.c) << 18 & 50529027) | (g << 26 & -50529028)) ^ g) <<
           12 &
           252645135) |
          (g << 20 & -252645136))) ^
        h;
      d.a =
        ((((h = (i = ((h = d.a) << 18 & 50529027) | (h << 26 & -50529028)) ^ h) <<
           12 &
           252645135) |
          (h << 20 & -252645136)) ^
         i) ^
        c;
      d.e =
        (k ^
         ((i = (o = ((i = d.d) << 18 & 50529027) | (i << 26 & -50529028)) ^ i) ^
          ((e << 12 & 252645135) | (e << 20 & -252645136)))) ^
        c;
      d.d =
        ((g ^ ((i << 12 & 252645135) | (i << 20 & -252645136))) ^ o) ^ c;
      d.b =
        ((h ^ ((f << 12 & 252645135) | (f << 20 & -252645136))) ^ l) ^ c;
      c = 0;
      loop L_h {
        e = c + d;
        e[0] = e[0] ^ (c + n)[0]:int;
        c = c + 4;
        if (c != 32) continue L_h;
      }
      f_e(d);
      d.h =
        ((f = (e = (c = d.g) << 24) ^ c) ^
         (c = (g = (c = d.h) << 24) ^ c) << 16) ^
        g;
      d.g = e ^ ((g = (h = (g = d.f) << 24) ^ g) ^ f << 16);
      d.f = h ^ ((e = (f = (e = d.e) << 24) ^ e) ^ g << 16);
      d.c =
        ((g = (h = (g = d.b) << 24) ^ g) ^
         (i = (k = (i = d.c) << 24) ^ i) << 16) ^
        k;
      d.a = ((k = (l = (k = d.a) << 24) ^ k) << 16 ^ l) ^ c;
      d.e = (f ^ ((l = (o = (l = d.d) << 24) ^ l) ^ e << 16)) ^ c;
      d.d = ((i ^ l << 16) ^ o) ^ c;
      d.b = ((k ^ g << 16) ^ h) ^ c;
      c = 0;
      loop L_i {
        e = c + d;
        e[0] = e[0] ^ (c + j)[0]:int;
        c = c + 4;
        if (c != 32) continue L_i;
      }
      j = j + 128;
      n = n + 128;
      p = p + 128;
      m = m + 128;
      q = q + 32;
      continue L_b;
    }
  }
}

function f_h(a:{ a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int }, b:int_ptr@1, c:int_ptr@1) {
  var d:int;
  var e:int;
  var i:int;
  var f:int;
  var g:int;
  var j:int;
  var l:int;
  var h:int;
  var k:int;
  var m:int;
  var n:int;
  var o:int;
  var p:int;
  a.h =
    (p = 
       ((d = 
           (l = 
              ((d = (i = ((d = c[12]) ^ (e = b[12]) >> 1) & 1431655765) ^ d) ^
               (f = (j = ((f = c[8]) ^ (g = b[8]) >> 1) & 1431655765) ^ f) >> 2) &
              858993459) ^
           d) ^
        (h = 
           (o = 
              ((h = (m = ((h = c[4]) ^ (k = b[4]) >> 1) & 1431655765) ^ h) ^
               (c = (n = ((c = c[0]) ^ (b = b[0]) >> 1) & 1431655765) ^ c) >> 2) &
              858993459) ^
           h) >>
        4) &
       252645135) ^
    d;
  a.g =
    (k = 
       ((d = (i = ((d = e ^ i << 1) ^ (e = g ^ j << 1) >> 2) & 858993459) ^ d) ^
        (g = (j = ((g = k ^ m << 1) ^ (b = b ^ n << 1) >> 2) & 858993459) ^ g) >>
        4) &
       252645135) ^
    d;
  a.f =
    (f = ((d = l << 2 ^ f) ^ (c = o << 2 ^ c) >> 4) & 252645135) ^ d;
  a.d = p << 4 ^ h;
  a.e =
    (e = ((d = i << 2 ^ e) ^ (b = j << 2 ^ b) >> 4) & 252645135) ^ d;
  a.c = k << 4 ^ g;
  a.b = f << 4 ^ c;
  a.a = e << 4 ^ b;
}

function f_i(a:{ a:int, b:int }, b:{ a:int, b:int }):int {
  var e:int;
  var d:int_ptr;
  if (b >= -65587 - (a = select_if(16, a, a <= 16))) goto B_a;
  var c:int_ptr = 
    f_b(a + (e = select_if(16, b + 11 & -8, b < 11)) + 12);
  if (eqz(c)) goto B_a;
  b = c - 8;
  d = a - 1;
  if (eqz(d & c)) {
    a = b;
    goto B_b;
  }
  var f:int_ptr = c - 4;
  var g:int = f[0];
  d = 
    (g & -8) -
    (c = 
       (a = (c = (c + d & 0 - a) - 8) + select_if(a, 0, c - b <= 16)) - b);
  if (g & 3) {
    a.b = (d | (a.b & 1)) | 2;
    d = a + d;
    d[1] = d[1] | 1;
    f[0] = (c | (f[0] & 1)) | 2;
    d = b + c;
    d[1] = d[1] | 1;
    f_d(b, c);
    goto B_b;
  }
  b = b.a;
  a.b = d;
  a.a = b + c;
  label B_b:
  b = a.b;
  if (eqz(b & 3)) goto B_e;
  c = b & -8;
  if (c <= e + 16) goto B_e;
  a.b = (e | (b & 1)) | 2;
  b = a + e;
  b.b = (e = c - e) | 3;
  c = a + c;
  c[1] = c[1] | 1;
  f_d(b, e);
  label B_e:
  d = a + 8;
  label B_a:
  return d;
}

function f_j(a:int_ptr, b:int_ptr) {
  var c:int_ptr;
  var f:int_ptr;
  var e:int_ptr;
  var d:int_ptr;
  if (b >= 256) {
    d = a[6];
    if (a == (b = a[3])) {
      c = (a + select_if(20, 16, b = a[5]))[0]:int;
      if (c) goto B_f;
      b = 0;
      goto B_e;
    }
    c = a[2];
    c[3] = b;
    b[2] = c;
    goto B_e;
    label B_f:
    e = select_if(a + 20, a + 16, b);
    loop L_h {
      f = e;
      b = c;
      e = select_if(b + 20, b + 16, c = b[5]);
      c = (b + select_if(20, 16, c))[0]:int;
      if (c) continue L_h;
    }
    f[0] = 0;
    label B_e:
    if (eqz(d)) goto B_b;
    c = a[7];
    e = (c << 2) + 1050276;
    if (e[0] != a) {
      if (d[4] == a) goto B_i;
      d[5] = b;
      if (b) goto B_c;
      goto B_b;
    }
    e[0] = b;
    if (eqz(b)) goto B_a;
    goto B_c;
    label B_i:
    d[4] = b;
    if (b) goto B_c;
    goto B_b;
  }
  c = a[3];
  if (c != (a = a[2])) {
    a[3] = c;
    c[2] = a;
    return ;
  }
  1050684[0]:int = 1050684[0]:int & -2 << (b >> 3);
  return ;
  label B_c:
  b[6] = d;
  c = a[4];
  if (c) {
    b[4] = c;
    c[6] = b;
  }
  a = a[5];
  if (eqz(a)) goto B_b;
  b[5] = a;
  a[6] = b;
  return ;
  label B_b:
  return ;
  label B_a:
  1050688[0]:int = 1050688[0]:int & -2 << c;
}

function f_k(a:{ a:int, b:int, c:int }, b:int):int {
  var d:int_ptr;
  var e:int;
  var f:int;
  var c:int = g_a - 16;
  g_a = c;
  if (b >= 128) {
    c[3]:int = 0;
    b = {
          if (b >= 2048) {
            if (b >= 65536) {
              c[15]:byte = (b & 63) | 128;
              c[12]:byte = b >> 18 | 240;
              c[14]:byte = (b >> 6 & 63) | 128;
              c[13]:byte = (b >> 12 & 63) | 128;
              c + 16;
              goto B_c;
            }
            c[14]:byte = (b & 63) | 128;
            c[12]:byte = b >> 12 | 224;
            c[13]:byte = (b >> 6 & 63) | 128;
            c + 12 | 3;
            goto B_c;
          }
          c[13]:byte = (b & 63) | 128;
          c[12]:byte = b >> 6 | 192;
          c + 12 | 2;
          label B_c:
        } -
        c + 12;
    if (b > a.a - (d = a.c)) {
      f_m(a, d, b);
      d = a.c;
    }
    if (b) { memory_copy(a.b + d, c + 12, b) }
    a.c = b + d;
    goto B_a;
  }
  var g:int = a.c;
  if (g == a.a) {
    d = g_a - 32;
    g_a = d;
    f = select_if(8, f = (e = a.a) << 1, f <= 8);
    if (f < 0) {
      f_ga(0, 0, 1049556);
      unreachable;
    }
    d[6] =
      if (e) {
        d[7] = e;
        d[5] = a.b;
        1;
      } else {
        0
      }
    f_q(d + 8, f, d + 20);
    if (d[2] == 1) {
      f_ga(d[3], d[4], 1049556);
      unreachable;
    }
    e = d[3];
    a.a = f;
    a.b = e;
    g_a = d + 32;
  }
  (a.b + g)[0]:byte = b;
  a.c = g + 1;
  label B_a:
  g_a = c + 16;
  return 0;
}

function f_l(a:int, b:int_ptr) {
  var d:int_ptr;
  var c:int_ptr = 31;
  a[4]:long@4 = 0L;
  if (b <= 16777215) { c = (b >> 6 - (d = clz(b >> 8)) & 1) - (d << 1) + 62 }
  a[7]:int = c;
  var e:int_ptr = (c << 2) + 1050276;
  d = 1 << c;
  if (eqz(d & 1050688[0]:int)) {
    e[0] = a;
    a[6]:int = e;
    1050688[0]:int = 1050688[0]:int | d;
    goto B_b;
  }
  if (b == ((d = e[0])[1] & -8)) {
    c = d;
    goto B_e;
  }
  var f:int = b << select_if(25 - (c >> 1), 0, c != 31);
  loop L_g {
    e = d + (f >> 29 & 4);
    c = e[4];
    if (eqz(c)) goto B_d;
    f = f << 1;
    d = c;
    if ((c[1] & -8) != b) continue L_g;
  }
  label B_e:
  b = c[2];
  b[3] = a;
  c[2] = a;
  a[6]:int = 0;
  a[3]:int = c;
  a[2]:int = b;
  return ;
  label B_d:
  (e + 16)[0]:int = a;
  a[6]:int = d;
  label B_b:
  a[3]:int = a;
  a[2]:int = a;
}

function f_m(a:{ a:int, b:int }, b:int, c:int) {
  var e:int;
  var g:int;
  var d:int_ptr = g_a - 32;
  g_a = d;
  if (b > (c = b + c)) goto B_b;
  e = select_if(8, c = select_if(c, e = (b = a.a) << 1, c > e), c <= 8);
  var h:long = i64_extend_i32_u(e);
  if (eqz(eqz(h >> 32L))) goto B_b;
  var f:int = i32_wrap_i64(h);
  if (f > 2147483647) goto B_b;
  d[6] =
    if (b) {
      d[7] = b;
      d[5] = a.b;
      1;
    } else {
      0
    }
  f_q(d + 8, f, d + 20);
  if (d[2] != 1) goto B_a;
  c = d[4];
  g = d[3];
  label B_b:
  f_ga(g, c, 1049488);
  unreachable;
  label B_a:
  b = d[3];
  a.a = e;
  a.b = b;
  g_a = d + 32;
}

function f_n(a:{ a:int, b:int }, b:int) {
  var f:long;
  var d:int;
  var c:int = g_a + -64;
  g_a = c;
  if (b[0]:int == -2147483648) {
    d = b[3]:int;
    var e:int_ptr = c + 36;
    e[0] = 0;
    c[7]:long@4 = 4294967296L;
    (c + 48)[0]:long = ((d = d[0]:int) + 8)[0]:long@4;
    (c + 56)[0]:long = (d + 16)[0]:long@4;
    c[5]:long = d[0]:long@4;
    f_f(c + 28, 1049572, c + 40);
    (c + 24)[0]:int = (d = e[0]);
    c[2]:long = (f = c[7]:long@4);
    (b + 8)[0]:int = d;
    b[0]:long@4 = f;
  }
  f = b[0]:long@4;
  b[0]:long@4 = 4294967296L;
  d = c + 8;
  d[0]:int = (b = b + 8)[0]:int;
  b[0]:int = 0;
  1050233[0]:ubyte;
  c[0]:long = f;
  b = f_na(12, 4);
  if (eqz(b)) {
    f_ya(4, 12);
    unreachable;
  }
  b[0]:long@4 = c[0]:long;
  (b + 8)[0]:int = d[0]:int;
  a.b = 1049596;
  a.a = b;
  g_a = c - -64;
}

function f_o(a:int, b:int_ptr, c:int, d:int, e:int) {
  var g:int;
  var f:int = g_a - 32;
  g_a = f;
  1050264[0]:int = (g = 1050264[0]:int) + 1;
  g = {
        0;
        if (g < 0) goto B_b;
        1;
        if (1050272[0]:ubyte) goto B_b;
        1050272[0]:byte = 1;
        1050268[0]:int = 1050268[0]:int + 1;
        2;
        label B_b:
      } &
      255;
  if (g != 2) {
    if (eqz(g & 1)) goto B_a;
    call_indirect(f + 8, a, b[6]);
    goto B_a;
  }
  g = 1050252[0]:int;
  if (g >= 0) {
    1050252[0]:int = g + 1;
    if (1050256[0]:int) {
      call_indirect(f, a, b[5]);
      f[29]:byte = e;
      f[28]:byte = d;
      f[6]:int = c;
      f[4]:long@4 = f[0]:long;
      call_indirect(1050256[0]:int, f + 16, (1050260[0]:int)[5]:int);
      goto B_e;
    }
    f[4]:int = -2147483648;
    f_ea(f + 16);
    label B_e:
    1050252[0]:int = 1050252[0]:int - 1;
    1050272[0]:byte = 0;
    if (eqz(d)) goto B_a;
    g_a = g_a - 16;
    unreachable;
  }
  label B_a:
  f[4]:int = -2147483648;
  f_ea(f + 16);
  unreachable;
}

function f_p(a:{ a:int, b:int }, b:int) {
  var f:long;
  var c:int = g_a - 48;
  g_a = c;
  if (b[0]:int == -2147483648) {
    var d:int = b[3]:int;
    var e:int_ptr = c + 20;
    e[0] = 0;
    c[3]:long@4 = 4294967296L;
    (c + 32)[0]:long = ((d = d[0]:int) + 8)[0]:long@4;
    (c + 40)[0]:long = (d + 16)[0]:long@4;
    c[3]:long = d[0]:long@4;
    f_f(c + 12, 1049572, c + 24);
    (c + 8)[0]:int = (d = e[0]);
    c[0]:long = (f = c[3]:long@4);
    (b + 8)[0]:int = d;
    b[0]:long@4 = f;
  }
  a.b = 1049596;
  a.a = b;
  g_a = c + 48;
}

function f_q(a:{ a:int, b:int, c:int }, b:int, c:{ a:int, b:int, c:int }) {
  if (b >= 0) {
    c = {
          if (c.b) {
            var d:int = c.c;
            if (d) {
              f_ja(c.a, d, 1, b);
              goto B_b;
            }
          }
          1;
          if (eqz(b)) goto B_b;
          1050233[0]:ubyte;
          f_na(b, 1);
          label B_b:
        }
    if (eqz(c)) {
      a.c = b;
      a.b = 1;
      a.a = 1;
      return ;
    }
    a.c = b;
    a.b = c;
    a.a = 0;
    return ;
  }
  a.b = 0;
  a.a = 1;
}

function f_r(a:int, b:{ a:int, b:int }):int {
  var c:long_ptr = g_a - 32;
  g_a = c;
  let t0 = 
    {
      if (a[0]:int != -2147483648) {
        f_la(b, a[1]:int, a[2]:int);
        goto B_a;
      }
      (c + 16)[0]:long = ((a = (a[3]:int)[0]:int) + 8)[0]:long@4;
      (c + 24)[0]:long = (a + 16)[0]:long@4;
      c[1] = a[0]:long@4;
      f_f(b.a, b.b, c + 8);
      label B_a:
    }
  g_a = c + 32;
  return t0;
}

function f_s(a:{ a:int, b:int }) {
  var f:int;
  var d:int = 1;
  var b:int_ptr = g_a - 16;
  g_a = b;
  var e:int_ptr = b + 12;
  var c:int = a.a;
  if (c) {
    b[3] = 1;
    d = a.b;
    e = b + 8;
    f = c;
  }
  e[0] = f;
  a = b[3];
  if (eqz(a)) goto B_b;
  c = b[2];
  if (eqz(c)) goto B_b;
  f_ta(d, c);
  label B_b:
  g_a = b + 16;
}

function f(a:int, b:int) {
  var c:int = g_a - 48;
  g_a = c;
  c[1]:int = 88;
  c[0]:int = a;
  c[3]:int = 2;
  c[2]:int = 1050168;
  c[5]:long@4 = 2L;
  c[5]:long = i64_extend_i32_u(c) | 12884901888L;
  c[4]:long = i64_extend_i32_u(c + 4) | 12884901888L;
  c[4]:int = c + 32;
  f_ca(c + 8, b);
  unreachable;
}

function f_u(a:int, b:int) {
  a = g_a - 48;
  g_a = a;
  if (eqz(1050232[0]:ubyte)) {
    g_a = a + 48;
    return ;
  }
  a[3]:int = 2;
  a[2]:int = 1049376;
  a[5]:long@4 = 1L;
  a[11]:int = b;
  a[4]:long = i64_extend_i32_u(a + 44) | 12884901888L;
  a[4]:int = a + 32;
  f_ca(a + 8, 1049416);
  unreachable;
}

function f_v(a:{ a:int, b:int, c:int }, b:int, c:int):int {
  var d:int;
  if (a.a - (d = a.c) < c) {
    f_m(a, d, c);
    d = a.c;
  }
  if (c) { memory_copy(a.b + d, b, c) }
  a.c = c + d;
  return 0;
}

function f_w(a:{ a:int, b:int }, b:{ a:int, b:int }) {
  1050233[0]:ubyte;
  var c:int = b.b;
  var d:int = b.a;
  b = f_na(8, 4);
  if (eqz(b)) {
    f_ya(4, 8);
    unreachable;
  }
  b.b = c;
  b.a = d;
  a.b = 1049612;
  a.a = b;
}

export function check_flag(a:int, b:int):int {
  var j:{ a:int, b:int, c:int }
  var d:int;
  var k:int_ptr;
  var e:int;
  var i:{ a:int, b:int, c:int }
  var f:int;
  var h:int;
  var p:int;
  var l:{ a:int, b:int }
  var ea:long;
  var z:int;
  var aa:int;
  var ca:int;
  var ga:long;
  var ha:long;
  var fa:long;
  var v:int;
  var da:int;
  var t:int;
  var x:int;
  var o:ubyte_ptr;
  var q:int_ptr = g_a - 32;
  g_a = q;
  var c:int = g_a - 32;
  g_a = c;
  c[7]:int = b;
  c[6]:int = a;
  c[5]:int = b;
  a = 0;
  var g:int_ptr = g_a - 16;
  g_a = g;
  l = c + 8;
  l.b =
    if ((b = (j = c + 20).c) < j.a) {
      d = 1;
      g_a = k = g_a - 16;
      e = k + 12;
      if (i = j.a) {
        k[3] = 1;
        f = j.b;
        e = k + 8;
        a = i;
      }
      h = g + 8;
      e[0]:int = a;
      if (a = k[3]) {
        i = k[2];
        if (eqz(b)) {
          if (eqz(i)) goto B_g;
          f_ta(f, i);
          goto B_g;
        }
        if (eqz(d = f_ja(f, i, a, e = b))) goto B_e;
        label B_g:
        j.a = b;
        j.b = d;
      }
      a = -2147483647;
      label B_e:
      h[1]:int = e;
      h[0]:int = a;
      g_a = k + 16;
      if ((a = g[2]) != -2147483647) goto B_b;
      j.c;
    } else {
      b
    }
  l.a = j.b;
  g_a = g + 16;
  goto B_a;
  label B_b:
  f_ga(a, g[3], 1049324);
  unreachable;
  label B_a:
  (q + 8)[0]:long = c[1]:long;
  g_a = c + 32;
  a = q[2];
  var r:{ a:int, b:int, c:int } = q + 20;
  r.c = (b = q[3]);
  r.b = a;
  r.a = b;
  let t3 = 
    {
      var m:int_ptr = g_a - 32;
      g_a = m;
      var u:{ a:int, b:int, c:int } = m + 8;
      var n:{ a:long, b:long, c:long, d:long } = r.b;
      l = r.c;
      j = 0;
      g = 0;
      k = 0;
      f = g_a - 816;
      g_a = f;
      (f + 424)[0]:long = d_calledResultunwraponanErrval[252]:long@1;
      f[52]:long = d_calledResultunwraponanErrval[244]:long@1;
      i = f + 432;
      e = g_a - 352;
      g_a = e;
      memory_fill(e + 32, 0, 320);
      f_h(e, a = f + 416, a);
      a = 8;
      loop L_j {
        c = a - 8;
        b = c + 15;
        d = e + (c << 2);
        c = 32;
        loop L_n {
          if (b - 8 >= 88) goto B_l;
          if (b >= 88) goto B_m;
          h = c + d;
          (h + 28)[0]:int = (h - 4)[0]:int;
          b = b - 1;
          c = c - 4;
          if (c) continue L_n;
        }
        goto B_k;
        label B_m:
        f(b, 1048992);
        unreachable;
        label B_l:
        f(b - 8, 1048976);
        unreachable;
        label B_k:
        b = e + k;
        c = b + 32;
        f_e(c);
        c[0]:int = c[0]:int ^ -1;
        c = b + 36;
        c[0]:int = c[0]:int ^ -1;
        c = b + 52;
        c[0]:int = c[0]:int ^ -1;
        b = b + 56;
        b[0]:int = b[0]:int ^ -1;
        b = e + g;
        if (j >= 8) {
          b[0]:int = b[0]:int ^ 49152;
          c = b + 4;
          c[0]:int = c[0]:int ^ 49152;
          c = b + 12;
          c[0]:int = c[0]:int ^ 49152;
          b = b + 16;
          b[0]:int = b[0]:int ^ 49152;
          goto B_o;
        }
        b = b + 32;
        b[0]:int = b[0]:int ^ 49152;
        label B_o:
        c = 0;
        d = -8;
        b = e + (a << 2);
        p = select_if(88, a, a >= 88) - 88;
        loop L_t {
          h = a + d;
          if (h >= 88) goto B_r;
          if (c == p) goto B_s;
          b[0]:int =
            ((((h = (b - 32)[0]:int ^ (b[0]:int >> 14 & 50529027)) << 2 & -50529028) ^
              (h << 4 & -252645136)) ^
             (h << 6 & -1061109568)) ^
            h;
          d = d + 1;
          b = b + 4;
          c = c - 1;
          if (c != -8) continue L_t;
        }
        goto B_q;
        label B_s:
        f(a - c, 1048960);
        unreachable;
        label B_r:
        f(h, 1048944);
        unreachable;
        label B_q:
        j = j + 1;
        g = g + 36;
        a = a + 8;
        k = k + 32;
        if (k != 320) continue L_j;
      }
      g = e + 96;
      k = e - -64;
      j = e + 32;
      a = 0;
      loop L_u {
        let t0 = a;
        a = 0;
        loop L_v {
          (c = a + j)[0]:int =
            ((c = ((c = c[0]:int) ^ (c = (c ^ c >> 4) & 51317760) << 4) ^ c) ^
             (c = (c ^ c >> 2) & 855651072) << 2) ^
            c;
          if ((a = a + 4) != 32) continue L_v;
        }
        a = 0;
        loop L_w {
          (c = a + k)[0]:int =
            ((c = c[0]:int) ^ (c = (c ^ c >> 4) & 251662080) << 4) ^ c;
          if ((a = a + 4) != 32) continue L_w;
        }
        a = 0;
        loop L_x {
          (c = a + g)[0]:int =
            ((c = ((c = c[0]:int) ^ (c = (c ^ c >> 4) & 202310400) << 4) ^ c) ^
             (c = (c ^ c >> 2) & 855651072) << 2) ^
            c;
          if ((a = a + 4) != 32) continue L_x;
        }
        g = g + 128;
        k = k + 128;
        j = j + 128;
        a = 1;
        if (eqz(t0 & 1)) continue L_u;
      }
      a = 288;
      loop L_y {
        b = a + e;
        b[0]:int =
          ((b = ((b = b[0]:int) ^ (b = (b ^ b >> 4) & 51317760) << 4) ^ b) ^
           (b = (b ^ b >> 2) & 855651072) << 2) ^
          b;
        a = a + 4;
        if (a != 320) continue L_y;
      }
      a = 0;
      loop L_z {
        b = a + e;
        c = b + 32;
        c[0]:int = c[0]:int ^ -1;
        c = b + 36;
        c[0]:int = c[0]:int ^ -1;
        c = b + 52;
        c[0]:int = c[0]:int ^ -1;
        b = b + 56;
        b[0]:int = b[0]:int ^ -1;
        a = a + 32;
        if (a != 320) continue L_z;
      }
      memory_copy(i, e, 352);
      g_a = e + 352;
      f[101]:long = 6869194837183520599L;
      f[100]:long = 5210488070931961695L;
      f[99]:long = 0L;
      f[98]:long = 0L;
      p = f + 384;
      f_ka(p);
      memory_copy(f, i, 384);
      f[400]:byte = 0;
      i.a =
        {
          if (eqz((ea = i64_extend_i32_u(l)) >> 32L)) {
            if ((a = i32_wrap_i64(ea)) <= 2147483647) goto B_ba
          }
          i.b = 0;
          1;
          goto B_aa;
          label B_ba:
          if (eqz(a)) {
            i.c = 1;
            i.b = 0;
            0;
            goto B_aa;
          }
          1050233[0]:ubyte;
          if (b = f_na(a, 1)) {
            i.c = b;
            i.b = l;
            0;
            goto B_aa;
          }
          i.c = a;
          i.b = 1;
          1;
          label B_aa:
        }
      var y:int = f[109]:int;
      if (f[108]:int != 1) {
        var s:int = f[110]:int;
        if (l) { memory_copy(s, n, l) }
        if (eqz(f[45]:long == -1L & (ea = f[44]:long) > -4294967297L)) {
          t = l & 15;
          e = l >> 4;
          goto B_ja;
        }
        e = l >> 4;
        if (e + ((t = l & 15) != 0) > (i32_wrap_i64(ea) ^ -1)) goto B_ga;
        label B_ja:
        f[111]:int = e;
        f[110]:int = s;
        f[109]:int = s;
        f[108]:int = (n = f + 352);
        d = g_a - 176;
        g_a = d;
        a = f + 432;
        var w:int = a[3]:int;
        let t1 = w & 1;
        z = a[2]:int;
        aa = a[1]:int;
        h = a[0]:int;
        if (w >= 2) {
          ca = w >> 1;
          c = d - -64;
          j = d + 128;
          k = d + 96;
          loop L_ma {
            f_da(d + 80);
            f_da(d + 112);
            g = 0;
            loop L_na {
              f_ka(d);
              (d + 152)[0]:long =
                (fa = (((ea = (ga = h[2]:long) + (ha = h[0]:long)) << 56L |
                        (ea & 65280L) << 40L) |
                       ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
                      (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
                       ((ea >> 40L & 65280L) | ea >> 56L)));
              d[1]:long = fa;
              d[0]:long =
                (ea = 
                   (((ea = i64_extend_i32_u(ea < ga) + (ga = h[1]:long) + h[3]:long) <<
                     56L |
                     (ea & 65280L) << 40L) |
                    ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
                   (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
                    ((ea >> 40L & 65280L) | ea >> 56L)));
              d[18]:long = ea;
              h[1]:long = ga + i64_extend_i32_u(eqz(ha = ha + 1L));
              h[0]:long = ha;
              ((a = (e = d + 112) + g) + 8)[0]:long@1 = fa;
              a[0]:long@1 = ea;
              if ((g = g + 16) != 32) continue L_na;
            }
            f_g(a = d + 80, f, e);
            (d + 136)[0]:long = ((b = aa + (da = v << 5)) + 24)[0]:long@1;
            (d + 128)[0]:long = (b + 16)[0]:long@1;
            (d + 120)[0]:long = (b + 8)[0]:long@1;
            d[14]:long = b[0]:long@1;
            f_da(b = d + 48);
            i = 1;
            loop L_oa {
              g = 0;
              loop L_pa {
                (b + g)[0]:byte = (a + g)[0]:ubyte ^ (e + g)[0]:ubyte;
                if ((g = g + 1) != 16) continue L_pa;
              }
              let t2 = i;
              i = 0;
              a = k;
              e = j;
              b = c;
              if (t2) continue L_oa;
            }
            (a = z + da)[0]:long@1 = d[48]:long@1;
            (a + 24)[0]:long@1 = (d + 72)[0]:long@1;
            (a + 16)[0]:long@1 = (d - -64)[0]:long@1;
            (a + 8)[0]:long@1 = (d + 56)[0]:long@1;
            if (ca != (v = v + 1)) continue L_ma;
          }
        }
        f_da(d);
        if (t1) {
          a = z + (b = (w & 268435454) << 4);
          f_ka(d + 160);
          h[0]:long = (fa = (ea = h[0]:long) + 1L);
          h[1]:long = (ga = h[1]:long) + i64_extend_i32_u(eqz(fa));
          d[21]:long =
            (((ea = ea + (fa = h[2]:long)) << 56L | (ea & 65280L) << 40L) |
             ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
            (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
             ((ea >> 40L & 65280L) | ea >> 56L));
          d[20]:long =
            (((ea = i64_extend_i32_u(ea < fa) + ga + h[3]:long) << 56L |
              (ea & 65280L) << 40L) |
             ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
            (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
             ((ea >> 40L & 65280L) | ea >> 56L));
          e = d + 80;
          f_da(e);
          (d + 88)[0]:long = d[21]:long;
          d[10]:long = d[20]:long;
          f_g(d + 112, f, e);
          (d + 8)[0]:long = (e = d + 120)[0]:long@1;
          d[0]:long = d[112]:long@1;
          e[0]:long = ((b = b + aa) + 8)[0]:long@1;
          d[14]:long = b[0]:long@1;
          f_ka(d + 32);
          g = 0;
          loop L_ra {
            (d + 32 + g)[0]:byte = (d + g)[0]:ubyte ^ (d + 112 + g)[0]:ubyte;
            g = g + 1;
            if (g != 16) continue L_ra;
          }
          a[0]:long@1 = d[32]:long@1;
          (a + 8)[0]:long@1 = (d + 40)[0]:long@1;
        }
        g_a = d + 176;
        if (t) {
          e = s + (l & -16);
          a = g_a - 80;
          g_a = a;
          f_ka(a - -64);
          n.a = (fa = (ea = n.a) + 1L);
          n.b = (ga = n.b) + i64_extend_i32_u(eqz(fa));
          a[9]:long =
            (((ea = ea + (fa = n.c)) << 56L | (ea & 65280L) << 40L) |
             ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
            (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
             ((ea >> 40L & 65280L) | ea >> 56L));
          a[8]:long =
            (((ea = i64_extend_i32_u(ea < fa) + ga + n.d) << 56L |
              (ea & 65280L) << 40L) |
             ((ea & 16711680L) << 24L | (ea & 4278190080L) << 8L)) |
            (((ea >> 8L & 4278190080L) | (ea >> 24L & 16711680L)) |
             ((ea >> 40L & 65280L) | ea >> 56L));
          f_da(a);
          (a + 8)[0]:long = a[9]:long;
          a[0]:long = a[8]:long;
          f_g(a + 32, f, a);
          (p + 8)[0]:long@1 = (a + 40)[0]:long@1;
          p[0]:long@1 = a[32]:long@1;
          g_a = a + 80;
          loop L_ta {
            e[0]:byte = p[0]:ubyte ^ e[0]:ubyte;
            e = e + 1;
            p = p + 1;
            t = t - 1;
            if (t) continue L_ta;
          }
        }
        u.c = l;
        u.b = s;
        u.a = y;
        g_a = f + 816;
        goto B_fa;
      }
      f_ga(y, f[110]:int, 1048812);
      unreachable;
      label B_ga:
      a = g_a + -64;
      g_a = a;
      a[3]:int = 43;
      a[2]:int = 1048592;
      a[5]:int = 1048576;
      a[4]:int = f + 432;
      a[7]:int = 2;
      a[6]:int = 1050188;
      a[9]:long@4 = 2L;
      a[7]:long = i64_extend_i32_u(a + 16) | 85899345920L;
      a[6]:long = i64_extend_i32_u(a + 8) | 90194313216L;
      a[8]:int = a + 48;
      f_ca(a + 24, 1048728);
      unreachable;
      label B_fa:
      1050233[0]:ubyte;
      b = f_na(56, 1);
      if (b) {
        b[48]:long@1 = 143009642011427521L;
        b[40]:long@1 = 6315395457821302550L;
        b[32]:long@1 = -1955905064672638357L;
        b[24]:long@1 = -8684071750392024005L;
        b[16]:long@1 = -8682618338371224816L;
        b[8]:long@1 = 2570840801305670777L;
        b[0]:long@1 = 3584201232957687288L;
        m[5] = 56;
        m[6] = b;
        m[7] = 56;
        if (m[4] == 56) {
          o = m[3];
          a = 56;
          loop L_xa {
            e = o[0];
            if (e == (i = b[0]:ubyte)) {
              o = o + 1;
              b = b + 1;
              a = a - 1;
              if (a) continue L_xa;
              goto B_wa;
            }
          }
          x = e - i;
          label B_wa:
          o = eqz(x);
        }
        f_s(m + 20);
        f_s(m + 8);
        f_s(r);
        g_a = m + 32;
        o;
        goto B_i;
      }
      f_ya(1, 56);
      unreachable;
      label B_i:
    }
  g_a = q + 32;
  return t3;
}

function f_y(a:int, b:int) {
  var c:int = g_a - 32;
  g_a = c;
  c[4]:int = 0;
  c[1]:int = 1;
  c[2]:long@4 = 4L;
  c[7]:int = 46;
  c[6]:int = a;
  c[0]:int = c + 24;
  f_ca(c, b);
  unreachable;
}

export function wbindgen_malloc(a:int, b:int):int {
  if (eqz(b) | eqz(f_ha(a, b))) goto B_a;
  if (a) {
    1050233[0]:ubyte;
    b = f_na(a, b);
    if (eqz(b)) goto B_a;
  }
  return b;
  label B_a:
  return unreachable;
}

function f_aa(a:int, b:int_ptr, c:int, d:int):int {
  if (c == 1114112) goto B_a;
  if (eqz(call_indirect(a, c, b[4]))) goto B_a;
  return 1;
  label B_a:
  if (eqz(d)) { return 0 }
  return call_indirect(a, d, 0, b[3]);
}

export function wbindgen_realloc(a:int, b:int, c:int, d:int):int {
  if (eqz(d) | eqz(f_ha(b, d))) goto B_a;
  a = f_ja(a, b, d, c);
  if (eqz(a)) goto B_a;
  return a;
  label B_a:
  return unreachable;
}

function f_ca(a:int, b:int) {
  var c:int = g_a - 16;
  g_a = c;
  c[6]:short = 1;
  c[2]:int = b;
  c[1]:int = a;
  b = g_a - 16;
  g_a = b;
  a = c + 4;
  var e:long = a[0]:long@4;
  b[3]:int = a;
  b[1]:long@4 = e;
  a = g_a - 16;
  g_a = a;
  b = b + 4;
  c = b[0]:int;
  var d:int = c[3]:int;
  br_table[B_d, B_c, ..B_b](c[1]:int)
  label B_d:
  if (d) goto B_b;
  c = 1;
  d = 0;
  goto B_a;
  label B_c:
  if (d) goto B_b;
  c = c[0]:int;
  d = c[1]:int;
  c = c[0]:int;
  goto B_a;
  label B_b:
  a[0]:int = -2147483648;
  a[3]:int = b;
  f_o(a, 1049860, b[1]:int, (a = b[2]:int)[8]:ubyte, a[9]:ubyte);
  unreachable;
  label B_a:
  a[1]:int = d;
  a[0]:int = c;
  f_o(a, 1049832, b[1]:int, (a = b[2]:int)[8]:ubyte, a[9]:ubyte);
  unreachable;
}

function f_da(a:long_ptr@1) {
  a[0] = 0L;
  (a + 24)[0]:long@1 = 0L;
  (a + 16)[0]:long@1 = 0L;
  (a + 8)[0]:long@1 = 0L;
}

function f_ea(a:{ a:int, b:int }) {
  var b:int = a.a;
  if (eqz(b == -2147483648 | eqz(b))) { f_ta(a.b, b) }
}

function f_fa(a:{ a:int, b:int }) {
  var b:int = a.a;
  if (b) { f_ta(a.b, b) }
}

function f_ga(a:int, b:int, c:int) {
  if (a) {
    f_ya(a, b);
    unreachable;
  }
  a = g_a - 32;
  g_a = a;
  a[6]:int = 0;
  a[3]:int = 1;
  a[2]:int = 1049908;
  a[4]:long@4 = 4L;
  f_ca(a + 8, c);
  unreachable;
}

function f_ha(a:int, b:int):int {
  return popcnt(b) == 1 & a <= -2147483648 - b
}

function f_ia(a:int) {
  a[4]:int = 0;
  a[2]:long@4 = 0L;
  a[0]:long@4 = 17179869184L;
}

function f_ja(a:int, b:int_ptr, c:{ a:int, b:int }, d:int):int {
  var h:int;
  return 
    {
      var f:int_ptr = a - 4;
      var e:int = f[0];
      var g:int = e & -8;
      if (g >= select_if(4, 8, e = e & 3) + b) {
        if (select_if(e, 0, (e = b + 39) < g)) goto B_d;
        if (c >= 9) {
          c = f_i(c, d);
          if (c) goto B_f;
          0;
          goto B_a;
        }
        b = 0;
        if (d > -65588) goto B_k;
        c = select_if(16, d + 11 & -8, d < 11);
        f = a - 4;
        h = f[0];
        e = h & -8;
        if (eqz(h & 3)) {
          if ((c < 256 | e < (c | 4)) | e - c >= 131073) goto B_l;
          a;
          goto B_h;
        }
        g = a - 8;
        var i:int_ptr = g + e;
        if (c > e) {
          if (i == 1050704[0]:int) goto B_n;
          if (i == 1050700[0]:int) goto B_p;
          h = i[1];
          if (h & 2) goto B_l;
          h = h & -8;
          e = h + e;
          if (e < c) goto B_l;
          f_j(i, h);
          d = e - c;
          if (d < 16) goto B_q;
          f[0] = (c | (f[0] & 1)) | 2;
          b = c + g;
          b[1] = d | 3;
          c = e + g;
          c.b = c.b | 1;
          goto B_i;
        }
        d = e - c;
        if (d > 15) goto B_o;
        a;
        goto B_h;
        label B_q:
        f[0] = (e | (f[0] & 1)) | 2;
        b = e + g;
        b[1] = b[1] | 1;
        a;
        goto B_h;
        label B_p:
        e = 1050692[0]:int + e;
        if (e < c) goto B_l;
        d = e - c;
        if (d <= 15) {
          f[0] = ((h & 1) | e) | 2;
          c = e + g;
          c.b = c.b | 1;
          d = 0;
          goto B_s;
        }
        f[0] = (c | (h & 1)) | 2;
        b = c + g;
        b[1] = d | 1;
        c = e + g;
        c.a = d;
        c.b = c.b & -2;
        label B_s:
        1050700[0]:int = b;
        1050692[0]:int = d;
        a;
        goto B_h;
        label B_o:
        f[0] = (c | (h & 1)) | 2;
        b = c + g;
        b[1] = d | 3;
        i[1] = i[1] | 1;
        goto B_i;
        label B_n:
        e = 1050696[0]:int + e;
        if (e > c) goto B_j;
        label B_l:
        c = f_b(d);
        if (eqz(c)) goto B_k;
        b = 
          select_if(d, b = select_if(-4, -8, (b = f[0]) & 3) + (b & -8), b > d);
        if (b) { memory_copy(c, a, b) }
        f_c(a);
        b = c;
        label B_k:
        b;
        goto B_h;
        label B_j:
        f[0] = (c | (h & 1)) | 2;
        1050704[0]:int = (b = c + g);
        1050696[0]:int = (c = e - c);
        b[1] = c | 1;
        a;
        goto B_h;
        label B_i:
        f_d(b, d);
        a;
        label B_h:
        goto B_a;
        label B_f:
        d = select_if(d, b, b > d);
        if (d) { memory_copy(c, a, d) }
        d = f[0];
        f = d & -8;
        if (f < b + select_if(4, 8, d = d & 3)) goto B_c;
        if (select_if(d, 0, e < f)) goto B_b;
        f_c(a);
        c;
        goto B_a;
      }
      f_y(1049689, 1049736);
      unreachable;
      label B_d:
      f_y(1049752, 1049800);
      unreachable;
      label B_c:
      f_y(1049689, 1049736);
      unreachable;
      label B_b:
      f_y(1049752, 1049800);
      unreachable;
      label B_a:
    }
}

function f_ka(a:long_ptr@1) {
  a[0] = 0L;
  (a + 8)[0]:long@1 = 0L;
}

function f_la(a:{ a:int, b:int }, b:int, c:int):int {
  return call_indirect(a.a, b, c, a.b[3]:int)
}

function f_ma(a:{ a:int, b:int }, b:int):int {
  return call_indirect(a.a, b, a.b[3]:int)
}

function f_na(a:int, b:int):int {
  return {
           if (b >= 9) {
             f_i(b, a);
             goto B_a;
           }
           f_b(a);
           label B_a:
         }
}

function f_oa(a:{ a:long, b:long }, b:int) {
  a.b = 7199936582794304877L;
  a.a = -5076933981314334344L;
}

function f_pa(a:{ a:long, b:long }, b:int) {
  a.b = -7465958581808515274L;
  a.a = -3461089016297083664L;
}

function f_qa(a:{ a:int, b:int }, b:int):int {
  return f_la(b, a.a, a.b)
}

function f_ra(a:{ a:int, b:int }, b:int) {
  a.b = 1049816;
  a.a = b;
}

function f_sa(a:int, b:{ a:int, b:int, c:int, d:ushort, e:ushort }):int {
  var l:int;
  var c:int;
  var d:{ a:byte, b:byte, c:byte }
  var e:int_ptr;
  var j:int;
  var f:byte_ptr;
  var h:int;
  var i:int = a[0]:int;
  var g:int = a[1]:int;
  var m:int = b.c;
  if (eqz(m & 402653184)) goto B_b;
  if (eqz(m & 268435456)) {
    if (g < 16) goto B_d;
    d = 
      {
        if (g < (l = (a = i + 3 & -4) - i)) goto B_h;
        h = g - l;
        if (h < 4) goto B_h;
        var k:int = h & 3;
        f = a == i;
        if (f) goto B_i;
        j = i - a;
        if (j <= -4) {
          loop L_k {
            c = c + ((a = d + i)[0]:byte > -65) + ((a + 1)[0]:byte > -65) +
                ((a + 2)[0]:byte > -65) +
                ((a + 3)[0]:byte > -65);
            d = d + 4;
            if (d) continue L_k;
          }
        }
        if (f) goto B_i;
        f = d + i;
        loop L_l {
          c = c + (f[0] > -65);
          f = f + 1;
          j = j + 1;
          if (j) continue L_l;
        }
        label B_i:
        a = i + l;
        if (eqz(k)) goto B_m;
        d = a + (h & -4);
        e = d.a > -65;
        if (k == 1) goto B_m;
        e = e + (d.b > -65);
        if (k == 2) goto B_m;
        e = e + (d.c > -65);
        label B_m:
        j = h >> 2;
        e = c + e;
        loop L_n {
          h = a;
          if (eqz(j)) goto B_g;
          d = select_if(192, j, j >= 192);
          k = d & 3;
          l = d << 2;
          f = 0;
          if (j >= 4) {
            var n:int = a + (l & 1008);
            c = a;
            loop L_p {
              a = c[0]:int;
              f = (((a ^ -1) >> 7 | a >> 6) & 16843009) + f +
                  ((((a = (c + 4)[0]:int) ^ -1) >> 7 | a >> 6) & 16843009) +
                  ((((a = (c + 8)[0]:int) ^ -1) >> 7 | a >> 6) & 16843009) +
                  ((((a = (c + 12)[0]:int) ^ -1) >> 7 | a >> 6) & 16843009);
              c = c + 16;
              if (c != n) continue L_p;
            }
          }
          j = j - d;
          a = h + l;
          e = (((f >> 8 & 16711935) + (f & 16711935)) * 65537 >> 16) + e;
          if (eqz(k)) continue L_n;
        }
        a = {
              a = h + ((d & 252) << 2);
              c = a[0]:int;
              c = ((c ^ -1) >> 7 | c >> 6) & 16843009;
              c;
              if (k == 1) goto B_q;
              c = c + ((((h = a[1]:int) ^ -1) >> 7 | h >> 6) & 16843009);
              c;
              if (k == 2) goto B_q;
              c + ((((a = a[2]:int) ^ -1) >> 7 | a >> 6) & 16843009);
              label B_q:
            }
        (((a >> 8 & 459007) + (a & 16711935)) * 65537 >> 16) + e;
        goto B_f;
        label B_h:
        0;
        if (eqz(g)) goto B_f;
        d = g & 3;
        if (g >= 4) {
          c = g & -4;
          loop L_s {
            e = e + ((a = f + i)[0]:byte > -65) + ((a + 1)[0]:byte > -65) +
                ((a + 2)[0]:byte > -65) +
                ((a + 3)[0]:byte > -65);
            if (c != (f = f + 4)) continue L_s;
          }
        }
        if (eqz(d)) goto B_g;
        c = f + i;
        loop L_t {
          e = e + (c[0]:byte > -65);
          c = c + 1;
          d = d - 1;
          if (d) continue L_t;
        }
        label B_g:
        e;
        label B_f:
      }
    goto B_c;
  }
  h = b.e;
  if (eqz(h)) {
    g = 0;
    goto B_v;
  }
  f = g + i;
  g = 0;
  c = h;
  a = i;
  loop L_x {
    d = a;
    if (d == f) goto B_u;
    g = g +
        (a = {
               a + 1;
               if ((e = a[0]:byte) >= 0) goto B_y;
               a + 2;
               if (e < -32) goto B_y;
               a + 3;
               if (e < -16) goto B_y;
               a + 4;
               label B_y:
             }) -
        d;
    c = c - 1;
    if (c) continue L_x;
  }
  label B_v:
  c = 0;
  label B_u:
  d = h - c;
  goto B_c;
  label B_d:
  if (eqz(g)) {
    g = 0;
    goto B_c;
  }
  h = g & 3;
  if (g >= 4) {
    e = g & 12;
    loop L_ba {
      d = d + ((a = c + i)[0]:byte > -65) + ((a + 1)[0]:byte > -65) +
          ((a + 2)[0]:byte > -65) +
          ((a + 3)[0]:byte > -65);
      if (e != (c = c + 4)) continue L_ba;
    }
  }
  if (eqz(h)) goto B_c;
  a = c + i;
  loop L_ca {
    d = d + (a[0]:byte > -65);
    a = a + 1;
    h = h - 1;
    if (h) continue L_ca;
  }
  label B_c:
  if (d >= (a = b.d)) goto B_b;
  h = a - d;
  d = 0;
  c = 0;
  br_table[B_fa, B_ea, ..B_da]((m >> 29 & 3) - 1)
  label B_fa:
  c = h;
  goto B_da;
  label B_ea:
  c = (h & 65534) >> 1;
  label B_da:
  f = m & 2097151;
  e = b.b;
  b = b.a;
  loop L_ga {
    if ((d & 65535) < (c & 65535)) {
      a = 1;
      d = d + 1;
      if (eqz(call_indirect(b, f, e[4]))) continue L_ga;
      goto B_a;
    }
  }
  a = 1;
  if (call_indirect(b, i, g, e[3])) goto B_a;
  d = 0;
  c = h - c & 65535;
  loop L_ia {
    i = d & 65535;
    a = i < c;
    if (c <= i) goto B_a;
    d = d + 1;
    if (eqz(call_indirect(b, f, e[4]))) continue L_ia;
  }
  goto B_a;
  label B_b:
  a = call_indirect(b.a, i, g, b.b[3]:int);
  label B_a:
  return a;
}

function f_ta(a:int, b:int) {
  var c:int = (a - 4)[0]:int;
  var d:int = c & -8;
  if (d >= select_if(4, 8, c = c & 3) + b) {
    if (select_if(c, 0, d > b + 39)) goto B_b;
    f_c(a);
    goto B_a;
  }
  f_y(1049689, 1049736);
  unreachable;
  label B_b:
  f_y(1049752, 1049800);
  unreachable;
  label B_a:
}

function f_ua(a:int_ptr, b:int_ptr):int {
  var g:int;
  var i:int;
  var j:int;
  var c:int_ptr;
  var m:long;
  var k:int_ptr;
  var f:int = a[0];
  var e:int = b;
  var h:int = g_a - 16;
  g_a = h;
  var d:int = 10;
  a = f;
  if (a >= 1000) {
    b = a;
    loop L_b {
      c = h + 6 + d;
      (c - 3)[0]:byte =
        ((j = (i = ((g = b - (a = b / 10000) * 10000) & 65535) / 100) << 1) +
         1049917)[0]:ubyte;
      (c - 4)[0]:byte = (j + 1049916)[0]:ubyte;
      (c - 1)[0]:byte =
        ((g = (g - i * 100 & 65535) << 1) + 1049917)[0]:ubyte;
      (c - 2)[0]:byte = (g + 1049916)[0]:ubyte;
      d = d - 4;
      let t0 = b > 9999999;
      b = a;
      if (t0) continue L_b;
    }
  }
  if (a <= 9) {
    b = a;
    goto B_c;
  }
  (d + h + 5)[0]:byte =
    ((a = (a - (b = (a & 65535) / 100) * 100 & 65535) << 1) + 1049917)[0]:ubyte;
  d = d - 2;
  (d + h + 6)[0]:byte = (a + 1049916)[0]:ubyte;
  label B_c:
  if (eqz(select_if(0, f, b))) {
    d = d - 1;
    (d + h + 6)[0]:byte = ((b << 1 & 30) + 1049917)[0]:ubyte;
  }
  let t1 = 
    {
      g = h + 6 + d;
      b = 0;
      i = select_if(43, 1114112, a = (c = e[2]:int) & 2097152);
      j = eqz(eqz(c & 8388608));
      var l:int = 10 - d;
      a = l + (a >> 21);
      if (a < (f = e[6]:ushort)) {
        if (eqz(c & 16777216)) {
          f = f - a;
          a = 0;
          br_table[B_l, B_k, B_l, ..B_j]((c >> 29 & 3) - 1)
          label B_l:
          a = f;
          goto B_j;
          label B_k:
          a = (f & 65534) >> 1;
          label B_j:
          k = c & 2097151;
          c = e[1]:int;
          e = e[0]:int;
          loop L_m {
            if ((b & 65535) < (a & 65535)) {
              d = 1;
              b = b + 1;
              if (eqz(call_indirect(e, k, c[4]))) continue L_m;
              goto B_g;
            }
          }
          d = 1;
          if (f_aa(e, c, i, j)) goto B_g;
          if (call_indirect(e, g, l, c[3])) goto B_g;
          b = 0;
          a = f - a & 65535;
          loop L_o {
            f = b & 65535;
            d = f < a;
            if (a <= f) goto B_g;
            b = b + 1;
            if (eqz(call_indirect(e, k, c[4]))) continue L_o;
          }
          goto B_g;
        }
        e[2]:int = (i32_wrap_i64(m = e[2]:long@4) & -1612709888) | 536870960;
        d = 1;
        c = e[0]:int;
        if (f_aa(c, k = e[1]:int, i, j)) goto B_g;
        a = f - a & 65535;
        loop L_p {
          if (a > (b & 65535)) {
            b = b + 1;
            if (eqz(call_indirect(c, 48, k[4]))) continue L_p;
            goto B_g;
          }
        }
        if (call_indirect(c, g, l, k[3])) goto B_g;
        e[2]:long@4 = m;
        0;
        goto B_f;
      }
      d = 1;
      a = e[0]:int;
      if (f_aa(a, b = e[1]:int, i, j)) goto B_g;
      d = call_indirect(a, g, l, b[3]);
      label B_g:
      d;
      label B_f:
    }
  g_a = h + 16;
  return t1;
}

function f_va(a:int, b:int):int {
  return f_la(b, 1048744, 17)
}

function f_wa(a:int, b:int):int {
  return f_f(a, 1049572, b)
}

function f_xa(a:long_ptr, b:long_ptr@4) {
  a[0] = b[0]
}

function f_ya(a:int, b:int) {
  call_indirect(a, b, select_if(a = 1050248[0]:int, 4, a));
  unreachable;
}

function f_za(a:int_ptr, b:int) {
  a[0] = 0
}

