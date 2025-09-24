import pytest
from click.testing import CliRunner 
# CliRunner allows you to simulate running a command-line program and capture its output, 
# so you can then assert that the output is what you expect.
from greedy_coin import main

def test_dollars_only():
    """Test the greedy coin algorithm with only a dollar amount."""
    runner = CliRunner()
    result = runner.invoke(main, ['--dollars', '2'])
    assert result.exit_code == 0  # Exit code of 0 signifies successful execution of the tool
    assert "Your change for 2.0: " in result.output
    assert "8 quarter" in result.output

def test_cents_only():
    """Test the greedy coin algorithm with only a cents amount."""
    runner = CliRunner()
    result = runner.invoke(main, ['--cents', '99'])
    assert result.exit_code == 0
    assert "Your change for 0.99: " in result.output
    assert "3 quarter" in result.output
    assert "2 dime" in result.output
    assert "4 penny" in result.output

def test_combined():
    """Test the greedy coin algorithm with dollars and cents."""
    runner = CliRunner()
    result = runner.invoke(main, ['--dollars', '1', '--cents', '50'])
    assert result.exit_code == 0
    assert "Your change for 1.5: " in result.output
    assert "6 quarter" in result.output
