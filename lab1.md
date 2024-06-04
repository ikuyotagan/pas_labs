# Лабораторная работа №1

**Цель работы:** Изучение команд для получения информации о системе и навыков работы с каталогами, файлами и правами доступа.

## Задание 1.1 Средства просмотра системной информации

### Цель: 
Изучение команд для получения информации о системе.

### Порядок выполнения:

1. **Отобразить используемую версию ядра**

   **Команда:** 
   ```sh
   itasm@pd uni % uname -r
   ```

   **Объяснение:** 
   Команда `uname -r` отображает текущую версию ядра операционной системы.

   ![uname -r](images/lab1/uname_r.png)

2. **Отобразить память занятую под дисковый кэш**

   **Команда:** 
   ```sh
   itasm@pd uni % vm_stat
   ```

   **Объяснение:** 
   Команда `vm_stat` отображает статистику использования виртуальной памяти, включая информацию о дисковом кэше.

   ![vm_stat](images/lab1/vm_stat.png)

## Задание 1.2 Команды для работы с каталогами, папками и файлами

### Цель:
Получить навыки работы с каталогами, папками и файлами.

### Порядок выполнения:

1. **Создать директорию и подтвердить создание**

   **Команды:**
   ```sh
   itasm@pd uni % mkdir ~/dir1
   itasm@pd uni % ls -l ~
   ```

   ![mkdir](images/lab1/mkdir.png)

2. **Создать в dir1 папки dir2 и dir4, а также dir3 внутри dir2**

   **Команды:**
   ```sh
   itasm@pd uni % mkdir ~/dir1/dir2 ~/dir1/dir4
   itasm@pd uni % mkdir ~/dir1/dir2/dir3
   itasm@pd uni % ls -l ~/dir1
   itasm@pd uni % ls -l ~/dir1/dir2
   ```

   ![mkdir_nested](images/lab1/mkdir_nested.png)

3. **Создать файлы file1 и file2 внутри dir3, создать файл file4**

   **Команды:**
   ```sh
   itasm@pd uni % touch ~/dir1/dir2/dir3/file1 ~/dir1/dir2/dir3/file2
   itasm@pd uni % ls -l ~/dir1/dir2/dir3
   ```

   ![touch](images/lab1/touch.png)

4. **Скопировать dir3 в dir1**

   **Команда:**
   ```sh
   itasm@pd uni % cp -r ~/dir1/dir2/dir3 ~/dir1/
   itasm@pd uni % ls -l ~/dir1
   ```

   ![cp](images/lab1/cp.png)

5. **Скопировать файл из dir3 в dir2 и удалить dir3**

   **Команды:**
   ```sh
   itasm@pd uni % cp ~/dir1/dir2/dir3/file2 ~/dir1/dir2/
   itasm@pd uni % rm -r ~/dir1/dir2/dir3
   itasm@pd uni % ls -l ~/dir1/dir2
   ```

   ![cp_rm](images/lab1/cp_rm.png)

6. **Переименовать file4 и переместить его в dir1**

   **Команды:**
   ```sh
   itasm@pd uni % mv ~/dir1/dir2/dir3/file4 ~/dir1/Empty
   itasm@pd uni % ls -l ~/dir1
   ```

   ![mv](images/lab1/mv.png)

7. **Переместить файлы из dir3 в dir4 и удалить пустую папку**

   **Команды:**
   ```sh
   itasm@pd uni % mv ~/dir1/dir3/file* ~/dir1/dir4/
   itasm@pd uni % rmdir ~/dir1/dir3
   itasm@pd uni % ls -l ~/dir1/dir4
   ```

   ![mv_rmdir](images/lab1/mv_rmdir.png)

8. **Создать и редактировать текстовый документ**

   **Команды:**
   ```sh
   itasm@pd uni % nano ~/dir1/finita
   ```

   **Содержимое файла:**
   ```
   Все задания выполнили. Команды для работы с папками файлами и каталогами выучили.
   ```

   ![nano](images/lab1/nano.png)

9. **Вывести содержимое файла finita в терминале**

   **Команда:**
   ```sh
   itasm@pd uni % cat ~/dir1/finita
   ```

   ![cat](images/lab1/cat.png)

## Задание 1.3 Управление правами доступа к файлам и каталогам

### Цель:
Получить навыки работы с правами доступа к файлам и каталогам.

### Порядок выполнения:

1. **Вывести полную информацию обо всех файлах из выбранной директории**

   **Команда:**
   ```sh
   itasm@pd uni % ls -l ~/dir1
   ```

   ![ls](images/lab1/ls.png)

2. **Удалить права на чтение и проанализировать результат**

   **Команды:**
   ```sh
   itasm@pd uni % chmod -r ~/dir1/finita
   itasm@pd uni % cat ~/dir1/finita
   ```

   Удаление прав на чтение лишает возможности чтения содержимого файла.

   ![chmod](images/lab1/chmod.png)

3. **Удалить права на запись и проанализировать результат**

   **Команды:**
   ```sh
   itasm@pd uni % chmod -w ~/dir1/finita
   itasm@pd uni % echo "Дополнение" >> ~/dir1/finita
   ```

   Удаление прав на запись лишает возможности изменения содержимого файла.

   ![chmod_write](images/lab1/chmod_write.png)

4. **Добавить право выполнения и проанализировать результат**

   **Команды:**
   ```sh
   itasm@pd uni % chmod +x ~/dir1/finita
   itasm@pd uni % ./dir1/finita
   ```

   Добавление прав на выполнение позволяет запустить файл как исполняемый, однако данный файл не является исполняемым.

   ![chmod_exec](images/lab1/chmod_exec.png)

5. **Создать и запустить скрипт hello_world.sh**

   **Команды:**
   ```sh
   itasm@pd uni % echo '#!/bin/bash' > ~/dir1/hello_world.sh
   itasm@pd uni % echo 'echo "Hello World"' >> ~/dir1/hello_world.sh
   itasm@pd uni % chmod 755 ~/dir1/hello_world.sh
   itasm@pd uni % ~/dir1/hello_world.sh
   ```

   ![hello_world](images/lab1/hello_world.png)

## Заключение

В ходе выполнения лабораторной работы были изучены команды для получения системной информации, а также команды для работы с каталогами, файлами и правами доступа в ОС macOS. Получены навыки использования терминала и различных команд для эффективного управления системой.