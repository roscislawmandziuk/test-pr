-- Tabela użytkowników
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela zgłoszeń
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    description TEXT,
    status VARCHAR(50),
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela komentarzy
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    ticket_id INT REFERENCES tickets(id),
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indeksy dla szybszego wyszukiwania
CREATE INDEX idx_tickets_status ON tickets(status);
CREATE INDEX idx_tickets_user_id ON tickets(user_id);
