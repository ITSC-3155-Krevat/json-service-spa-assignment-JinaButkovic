CREATE DATABASE IF NOT EXISTS module_13_library;

USE module_13_library;

CREATE TABLE IF NOT EXISTS book (
    book_id INT          AUTO_INCREMENT,
    title   VARCHAR(255) NOT NULL,
    author  VARCHAR(255) NOT NULL,
    rating  INT          NOT NULL,
    PRIMARY KEY (book_id)
);
