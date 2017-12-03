def test_default(cookies):
    """
    Checks if default configuration is working
    """
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.project.isdir()
    assert result.exception is None
