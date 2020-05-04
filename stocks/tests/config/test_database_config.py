from config import database_config


def test_config_path():
    assert database_config._config_path is not None


def test_database_config_path():
    assert database_config._database_config_path is not None


def test_username():
    assert database_config.username is not None


def test_host():
    assert database_config.host is not None


def test_port():
    assert database_config.port is not None


def test_database():
    assert database_config.database is not None


def test_test_database():
    assert database_config.test_database is not None
