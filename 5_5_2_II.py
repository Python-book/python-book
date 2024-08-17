set_1_alias = set_1 = {1, "2", 3.0}
set_2_alias = set_2 = {3, "4", 1}
print(f"# {set_1=}, {set_2=}, {set_1 | set_2=}")
# set_1={1, 3.0, '2'}, set_2={1, '4', 3}, set_1 | set_2={1, 3.0, '4', '2'}

set_1 |= set_2
print(f"# {set_1=}, {set_1 is set_1_alias=}")
# set_1={1, 3.0, '4', '2'}, set_1 is set_1_alias=True

set_2 |= set_1
print(f"# {set_2=}, {set_2 is set_2_alias=}")
# set_2={1, 3, '4', '2'}, set_2 is set_2_alias=True
