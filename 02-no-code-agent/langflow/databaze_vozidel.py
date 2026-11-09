import json
import sqlite3

from langflow.custom import Component
from langflow.io import MessageTextInput, Output, StrInput
from langflow.schema.message import Message


class DatabazeVozidel(Component):
    display_name = "Databáze vozidel (SQLite)"
    description = "Spustí jeden SELECT nad tabulkami lokality, vozidla, rezervace a vrátí řádky jako JSON."
    icon = "database"
    name = "DatabazeVozidel"

    inputs = [
        StrInput(name="db_path", display_name="Cesta k databázi", value="vozidla.db", advanced=True),
        MessageTextInput(
            name="sql_dotaz",
            display_name="SQL dotaz",
            info="Jeden SELECT dotaz (SQLite) nad tabulkami lokality, vozidla, rezervace.",
            tool_mode=True,
        ),
    ]

    outputs = [Output(display_name="Výsledek", name="vysledek", method="spustit_dotaz")]

    def spustit_dotaz(self) -> Message:
        dotaz = (self.sql_dotaz or "").strip().rstrip(";").strip()

        # povolen jen jeden SELECT
        if not dotaz.lower().startswith(("select", "with")) or ";" in dotaz:
            return Message(text="Chyba: povolen je pouze jeden SELECT dotaz.")

        try:
            # mode=ro -> databáze jen pro čtení
            with sqlite3.connect(f"file:{self.db_path}?mode=ro", uri=True) as conn:
                conn.row_factory = sqlite3.Row
                radky = [dict(r) for r in conn.execute(dotaz).fetchmany(200)]
        except sqlite3.Error as e:
            return Message(text=f"Chyba SQL: {e}")

        if not radky:
            return Message(text="Dotaz nevrátil žádné řádky.")
        return Message(text=json.dumps(radky, ensure_ascii=False, default=str))