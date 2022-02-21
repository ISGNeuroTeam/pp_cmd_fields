from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd


class FieldsCommand(BaseCommand):
    """Fields command with sequestered logics. To be improved. """

    syntax = Syntax(
        [Rule(name="field", type="arg", input_types=['string', 'term'], inf=True, )],  # must_be_a_field=True
        use_timewindow=False
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        fields = self.get_arg('col', all=True)

        return df[[field.value for field in fields]]
