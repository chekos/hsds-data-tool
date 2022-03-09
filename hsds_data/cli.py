from pathlib import Path

import typer
import pandas as pd
from rich.console import Console

from .hsds_schemas import HSDS_SCHEMAS_ENUM, HSDS_SCHEMAS_DICT

cli = typer.Typer()
__app_name__ = "hsds-data"
console = Console()


@cli.command()
def validate(
    csv_filepath: Path = typer.Argument(
        ...,
        help="CSV file to validate.",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
    schema_name: HSDS_SCHEMAS_ENUM = typer.Argument(
        ..., help="Schema to validate CSV against."
    ),
):
    """Validate a CSV file against the official HSDS schema."""
    console.print(
        f"Validating [magenta]{csv_filepath}[/magenta] against [yellow]{schema_name}[/yellow]"
    )
    data = pd.read_csv(csv_filepath)
    for col in data.select_dtypes("object").columns:
        data[col] = data[col].astype("string")
    for col in data.select_dtypes("float64").columns:
        if data[col].isna().all():
            data[col] = data[col].astype("string")
    schema = HSDS_SCHEMAS_DICT[f"{schema_name}_schema"]
    console.print(schema.validate(data, lazy=True).head())
        


def _version_callback(value: bool) -> None:
    if value:
        console.print("0.1")
        raise typer.Exit()


@cli.callback(invoke_without_command=True)
def version(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    pass


if __name__ == "__main__":
    cli()
