import pandas as pd
from pp_exec_env.base_command import BaseCommand, Syntax
from otlang.sdk.syntax import Positional, OTLType


class FieldsCommand(BaseCommand):
    """Fields command with sequestered logics. To be improved."""

    syntax = Syntax([Positional("field", otl_type=OTLType.TEXT, inf=True)])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        fields = self.get_iter('col')
        return df[[field.value for field in fields]]
