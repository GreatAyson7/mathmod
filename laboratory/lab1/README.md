# Лабораторная работа №1
Цель работы: показать возможности программы git.
## Ход работы:
### 1) Создаём SSH-ключ для работы с GitHub:
#### Создаём ключ
``` bash
ssh-keygen -t rsa -C "1032180470@pfur.ru"
```
#### Находим ключ
Переходим в папку с ключом ~/.ssh и с помощью команды "cat" выводим содержимое файла id_rsa.pub на экран.
### 2) Создаём необходимые папки и создаём репозиторий:
#### С помощью команды mkdir создаем папки
```bash
mkdir 2021
cd 2021
mkdir mathmode
cd mathmode
mkdir lab1
cd lab1
```
#### Создадим в папке mathmode файл "README.md" и запишем в него что-нибудь
```bash
cd .. 
touch README.md
```
#### Создаем репозиторий
```bash
git init
git add README.md
git commit -m "add first commit"
git status
```
### 3) Скачивание шаблона и написание отчёта:
Скачаем с ТУИСа шаблон отчета и скопируем его в папку "lab1" и изменяем его. Затем выполняем выгружаем всё на удаленный репозиторий:
```bash
git add lab1
git commit "change lab1"
git push -u origin mathmode
```

## Ссылки на Youtube и Github:
### 1) https://youtu.be/U98Xj1zCglg
### 2) https://github.com/GreatAyson7/mathmod
