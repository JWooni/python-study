BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regDate text);
INSERT INTO "users" VALUES(1,'Kim','jwooni@google.com','010-0000-0000','JWooni.com','2021-06-16 16:49:21');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-1234-5678','park.com','2021-06-16 16:56:21');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-06-16 17:04:07');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2021-06-16 17:04:07');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2021-06-16 17:04:07');
COMMIT;
