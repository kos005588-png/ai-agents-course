New Flow → Blank Flow.
Přidej komponenty Chat Input, Agent, Chat Output a Calculator.
Přes New Custom Component vlož kód z databaze_vozidel.py
U komponenty Databáze vozidel a u Calculatoru zapni Tool Mode a oba výstupy připoj do vstupu Tools u Agenta.
Zapoj Chat Input do Agenta a Agenta do Chat Outputu.
V Agent Instructions použij stejný text jako systemMessage v n8n, jen bez první části s {{ $now… }}.
Klikni na Export, ale bez volby „Save with my API keys“.
Výsledek ulož jako 02-no-code-agent/langflow/agent_vozovy_park_langflow.json.