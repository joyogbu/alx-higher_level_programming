-- convert database to utf8mb4
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- for table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- for column
ALTER TABLE first_table CHANGE COLUMN name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
