CREATE EXTENSION IF NOT EXISTS pgvector;

CREATE TABLE document(
	doc_id VARCHAR(1024) PRIMARY KEY,
	doc_name TEXT,
	description TEXT,
	embedding vector(1536));