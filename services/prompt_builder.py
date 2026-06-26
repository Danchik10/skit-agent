from models.diagnostic import DiagnosticResult


class PromptBuilder:

    PROMPTS = {

        "cpu": """
Ты DevOps инженер.

Проанализируй вывод команды Linux.

Определи:

- главный процесс,
- возможную причину,
- рекомендацию.

Ответ максимум три предложения.

Диагностика:

{diagnostics}
""",

        "service": """
Ты опытный DevOps инженер.

Проанализируй состояние сервиса.

Определи:

1. Почему сервис недоступен.
2. Какая ошибка встречается в логах.
3. Что рекомендуется сделать.

Данные диагностики:

{diagnostics}

Ответ должен быть не длиннее трех предложений.
"""
    }

    @classmethod
    def build(cls, diagnostic: DiagnosticResult) -> str:

        template = cls.PROMPTS.get(diagnostic.event_type)

        if template is None:
            raise ValueError(
                f"Неизвестный тип события: {diagnostic.event_type}"
            )

        return template.format(
            diagnostics=diagnostic.diagnostics
        )