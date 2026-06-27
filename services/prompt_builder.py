from models.diagnostic import DiagnosticResult


class PromptBuilder:
    PROMPTS = {

        "cpu": """
Ты системный администратор Linux.

Ниже приведён вывод диагностических команд.

Ответь строго в формате:

Причина:
...

Что обнаружено:
...

Рекомендация:
...

Не повторяй текст задания.
Не пересказывай вопрос.
Не придумывай данные.

Диагностика:

{diagnostics}
    """,

        "disk": """
    Ты DevOps инженер.

    Проанализируй использование дискового пространства.

    Определи:

    - какая файловая система почти заполнена;
    - какие каталоги занимают больше всего места;
    - что рекомендуется очистить или проверить.

    Ответ максимум три предложения.

    Диагностика:

    {diagnostics}
    """,

        "service": """
 Ты DevOps инженер.

Тебе дан вывод команды systemctl и последние строки журнала.

Определи:

Причина:
...

Ошибка:
...

Рекомендация:
...

Не переписывай текст задания.
Используй только информацию из диагностики.

Диагностика:

{diagnostics}
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