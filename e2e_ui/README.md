## Запуск автоматического теста E2E UI и просмотр отчетов Allure для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium.

### Тест умеет проверять процесс от автоматизации до завершения покупки.

С сайта github.com клонируйте репозиторий, в используемую вами IDE, следующей командой:
```html
git clone https://github.com/DenNikiten/TaskEM.git
```

### Создайте виртуальное окружение с помощью следующих команд:

В терминале в рабочей директории e2e_ui выполните команду для Windows, Linux и macOS:
```html
python -m venv venv
```

### Активируйте виртуальное окружение с помощью следующих команд:

В терминале в рабочей директории e2e_ui выполните команду для Windows:
```html
venv\Scripts\activate
```

В терминале в рабочей директории e2e_ui выполните команду для Linux и macOS:
```html
source venv/bin/activate
```

### В терминале в рабочей директории e2e_ui установите зависимости для работы следующей командой:
```html
pip install -r requirements.txt
```

При работе в Windows, переходим к выполнению команды для запуска тестов и создания Allure отчетов в папке test_results/.

При работе в Linux и macOS, меняем данные в модулях, а именно пути:
1. В папке tests в модуле conftest.py строку 'with open(r".\yaml_files\datatest.yaml", encoding="utf-8") as f:' меняем на 'with open(r"./yaml_files/datatest.yaml", encoding="utf-8") as f:'
2. В папке utilities в модуле logger.py строку 'file_name = r".\logs\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"' меняем на 'file_name = r"./logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"'
3. В папке base в модуле base_page.py в методе get_screenshot() строку "path = '.\\screen\\'" меняем на "path = r'./screen/'"
 

### В терминале в директории проекта e2e_ui выполните команду для запуска тестов и создания Allure отчетов в папке test_results/:
```html
python -m pytest --alluredir=test_results/
```

### Для просмотра отчетов Allure в директории проекта e2e_ui в терминале выполните команду:
```html
allure serve test_results/
```
