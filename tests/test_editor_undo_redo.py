import pytest
import gameplay.editor_undo_redo as mod

CASES = [
    ("remote_insert", (1,)),
    ("save_race", (1,)),
    ("batch_coalesce", (1,)),
    ("stack_cap", (1,)),
    ("cross_scene", (1,)),
    ("determinism", (1,)),
    ("command_apply", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("cursor", (1,)),
    ("metrics", (1,)),
    ("snapshot", (1,)),
    ("replay", (1,)),
    ("conflict", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
