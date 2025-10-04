import pytest
from services.ai_service import generate_script

def test_generate_script():
    prompt = "Generate a script about AI."
    script = generate_script(prompt)
    assert isinstance(script, str)
    assert len(script) > 0
