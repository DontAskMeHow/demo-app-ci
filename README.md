# demo-app-ci

Минимальное демо полного конвейера GitLab CI для k3s: Python-приложение с
pytest-тестами, сборка артефакта и деплой в k3s-кластер манифестами через
GitLab Kubernetes-агента.

## Структура

```
app.py                 приложение (тривиальная функция + main)
k3s/                   манифесты k3s: ConfigMap (код), Deployment, Service
tests/                 pytest (test_app.py + conftest.py)
.gitlab-ci.yml         конвейер: test → build → deploy
```

## Конвейер

- `test_job` — python:3.11, `pytest -v`, junit-отчёт артефактом;
- `build_job` — упаковывает `app.zip` из `app.py`;
- `deploy_job` — bitnami/kubectl, применяет манифесты `k3s/` через
  k3s-агента GitLab (`environment.name = demo-k3s`). Перед первым
  запуском зарегистрируйте в GitLab своего агента и замените
  `agent: k3s-demo` и context на свои.

## Локально

```bash
pip install -r requirements.txt
pytest -v
python app.py   # -> 5
```

## Лицензия

MIT — см. [LICENSE](LICENSE).
