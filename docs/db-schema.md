# Schemat bazy danych

## Tabela users
- id – klucz główny
- name – imię użytkownika
- email – unikalny adres email
- created_at – data utworzenia

## Tabela tickets
- id – klucz główny
- title – tytuł zgłoszenia
- description – opis
- status – status zgłoszenia
- user_id – klucz obcy do users.id
- created_at – data utworzenia

## Tabela comments
- id – klucz główny
- content – treść komentarza
- ticket_id – klucz obcy do tickets.id
- user_id – klucz obcy do users.id
- created_at – data dodania
