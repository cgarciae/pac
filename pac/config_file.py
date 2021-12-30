import typing as tp
from importlib.machinery import SourceFileLoader
from pathlib import Path

import typing_extensions as tpe
from pydantic import BaseModel

C = tp.TypeVar("C", bound="ConfigFile")


class ConfigFile(BaseModel):
    """"""

    filepath: Path

    @classmethod
    def load(
        cls: tp.Type[C],
        path: tp.Union[str, Path],
        module_name: tp.Optional[str] = None,
    ) -> C:
        """Load model configurations stored as *.py files. The config file is loaded and validated against the input Schema class.

        Args:
            path: Path to the config file.
            module_name: Name of the module to load. If not specified, the filename is used.

        Returns:
            ConfigFile instance.
        """

        path_: Path = Path(path)

        if not path_.exists():
            raise ValueError(f"File '{path_}' not found")

        # load python file form a path
        config_module = SourceFileLoader(
            fullname=module_name if module_name is not None else path_.stem,
            path=str(path_),
        ).load_module()

        config = cls(
            filepath=path_,
            **vars(config_module),
        )

        return config
