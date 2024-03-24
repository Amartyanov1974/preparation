update: ## Обновляет local-окружение: скачивает и пересобирает докер-образы
	docker compose pull --ignore-buildable
	docker compose build
	@echo "Update done successfully."

help: ## Отображает список доступных команд и их описания
	@echo "Cписок доступных команд:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
