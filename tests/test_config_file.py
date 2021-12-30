import typing as tp

from pac import ConfigFile


class Experiment(ConfigFile):
    a: int
    b: float
    c: tp.Callable[[], dict]


class TestConfigFile:
    def test_sample_config(self):

        config = Experiment.load(
            path="tests/sample_config.py",
        )

        assert config.a == 1
        assert config.b == 2.0
        assert config.c() == {"a": 1, "b": 2.0}
