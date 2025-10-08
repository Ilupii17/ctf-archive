from pwn import *
import re

p = process('/challenge/run')

class Level:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

class Category:
    def __init__(self, name: str, bit: int):
        self.name = name
        self.bit = bit

def is_subset(a, b):
    return (b | a) == b

def solve_question(question_line, levels_map, categories_map):
    q_line = question_line
    
    pattern_with_cats = r"Can a Subject with level (\S+) and categories {([^}]*)} (read|write) an Object with level (\S+) and categories {([^}]*)}\?"
    pattern_no_cats = r"Can a Subject with level (\S+) (read|write) an Object with level (\S+)\?"

    m = re.search(pattern_with_cats, q_line)
    if m:
        s_level_name, s_cat_str, action, o_level_name, o_cat_str = m.groups()
    else:
        m = re.search(pattern_no_cats, q_line)
        if not m:
            log.error(f"Gagal mem-parsing pertanyaan: {q_line}")
            return
        s_level_name, action, o_level_name = m.groups()
        s_cat_str, o_cat_str = "", ""

    s_level = levels_map.get(s_level_name, 0)
    o_level = levels_map.get(o_level_name, 0)
    
    s_cat_set = sum(categories_map.get(c.strip(), 0) for c in s_cat_str.split(',') if c)
    o_cat_set = sum(categories_map.get(c.strip(), 0) for c in o_cat_str.split(',') if c)
    
    is_allowed = False
    if action == "read":
        if s_level >= o_level:
            if not categories_map or is_subset(o_cat_set, s_cat_set):
                is_allowed = True
    elif action == "write":
        if o_level >= s_level:
            if not categories_map or is_subset(s_cat_set, o_cat_set):
                is_allowed = True
    
    answer = b"yes" if is_allowed else b"no"
    p.sendlineafter(b"?", answer)
    log.info(f"Answered: {answer.decode()}")
    p.recvline()

try:
    p.recvuntil(b"to answer ")
    num_questions = int(p.recvuntil(b" questions", drop=True))
    log.info(f"Number of questions: {num_questions}")

    p.recvuntil(b"system:\n")
    setup_and_q1_raw = p.recvuntil(b"?\n").decode()

    q1_separator = "Q 1. "
    setup_raw, _, q1_raw = setup_and_q1_raw.rpartition(q1_separator)
    q1_full = q1_separator + q1_raw

    if "Categories:" in setup_raw:
        levels_part, categories_part = setup_raw.split("Categories:")
        level_data = [line for line in levels_part.strip().split('\n')[1:] if line]
        category_data = [line for line in categories_part.strip().split('\n') if line]
    else:
        level_data = [line for line in setup_raw.strip().split('\n')[1:] if line]
        category_data = []

    levels = {name: (len(level_data) - i) for i, name in enumerate(level_data)}
    log.info(f"Levels parsed: {levels}")
    
    categories = {name: (1 << i) for i, name in enumerate(category_data)}
    log.info(f"Categories parsed: {categories}")

    log.info("Solving Q1...")
    solve_question(q1_full, levels, categories)

    for i in range(1, num_questions):
        question_line = p.recvuntil(b"?\n")
        log.info(f"Solving Q{i+1}...")
        solve_question(question_line.decode(), levels, categories)

    log.success("All questions answered!")
    print(p.recvall().decode())

except Exception as e:
    log.error(f"An error occurred: {e}")
    print(p.recvall(timeout=1).decode())
finally:
    p.close()