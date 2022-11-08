import pandas as pd
from pp_exec_env.base_command import BaseCommand, Syntax
from otlang.sdk.syntax import Positional, OTLType


class FieldsCommand(BaseCommand):
    """Fields command with sequestered logics. To be improved."""

    syntax = Syntax([Positional("fields", otl_type=OTLType.TEXT, inf=True)])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        fields = self.get_iter('fields')

        # dataframe can be changed, so if columns disappears no need for exception
        fields = filter(lambda x: x.value in df.columns, fields)

        return df[[field.value for field in fields]]
