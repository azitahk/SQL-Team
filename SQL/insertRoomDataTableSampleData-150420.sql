#https://www.mysqltutorial.org/mysql-insert-multiple-rows/

INSERT INTO roomData (roomName, humidity, temperature, readDate)
VALUES 
('E223', '47.63', '27.64', NOW()),
('E223', '47.58', '27.60', ADDTIME(now(), '01:00:00')),
('E223', '47.52', '27.63', ADDTIME(now(), '02:00:00'));