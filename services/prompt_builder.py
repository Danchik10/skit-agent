from models.diagnostic import DiagnosticResult


class PromptBuilder:

    PROMPTS = {

        "cpu": """
Ты опытный DevOps инженер.

Проанализируй список процессов.

Определи:

1. Какой процесс создает основную нагрузку на CPU.
2. Возможную причину высокой нагрузки.
3. Что рекомендуется сделать администратору.

Данные диагностики:

{diagnostics}

Ответ должен быть не длиннее трех предложений.
""",

        "disk": """
Ты опытный DevOps инженер.

Проанализируй использование дискового пространства.

Определи:

1. Какая файловая система переполнена.
2. Какие каталоги занимают больше всего места.
3. Что рекомендуется очистить или проверить.

Данные диагностики:

{diagnostics}

Ответ должен быть не длиннее трех предложений.
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