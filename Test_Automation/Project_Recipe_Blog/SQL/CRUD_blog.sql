use blog;

-- segéd rekordok
INSERT INTO category (category_id, name) VALUES (null, '_pohár');
SET @categoryID_ins = (SELECT category_id FROM category WHERE name = '_pohár');
INSERT INTO category (category_id, name) VALUES (null, '_bögre');
SET @categoryID_upd = (SELECT category_id FROM category WHERE name = '_bögre');

INSERT INTO roles (role_id, authority) VALUES (null, '_vendég');
SET @roleID_ins = (SELECT role_id FROM roles WHERE authority = '_vendég');
INSERT INTO roles (role_id, authority) VALUES (null, '_pincér');
SET @roleID_upd = (SELECT role_id FROM roles WHERE authority = '_pincér');

INSERT INTO user (user_id, email, name, password, enabled, mfa_enabled) VALUES (null, '_userins@hhh.hu', 'User1', 'password1', 1, 1);
SET @userID_ins = (SELECT user_id FROM user WHERE email = '_userins@hhh.hu');
INSERT INTO user (user_id, email, name, password, enabled, mfa_enabled) VALUES (null, '_userupd@hhh.hu', 'User2', 'password2', 1, 1);
SET @userID_upd = (SELECT user_id FROM user WHERE email = '_userupd@hhh.hu');

INSERT INTO recipe (recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves)
			VALUES (null, now(), date_add(now(), INTERVAL 10 DAY), 'Itt következik a receptről egy hosszú leírás', date_add(now(), INTERVAL 1 DAY), '_Teszt receptem1', @categoryID_ins, @userID_ins, 1, 2, 30, 'Finom', 0); -- beszúrás
SET @recipeID_ins = (SELECT recipe_id FROM recipe WHERE title = '_Teszt receptem1'); -- azonosító lekérése
INSERT INTO recipe (recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves)
			VALUES (null, now(), date_add(now(), INTERVAL 10 DAY), 'Itt következik a receptről egy hosszú, pontos leírás', date_add(now(), INTERVAL 1 DAY), '_Teszt receptem2', @categoryID_ipd, @userID_upd, 1, 2, 30, 'Finom', 0); -- beszúrás
SET @recipeID_upd = (SELECT recipe_id FROM recipe WHERE title = '_Teszt receptem2'); -- azonosító lekérése


-- category tábla
INSERT INTO category (category_id, name) VALUES (null, '_alma'); -- beszúrás
SELECT category_id, name FROM category WHERE name = '_alma'; -- beszúrás ellenőrzés
SET @categoryID = (SELECT category_id FROM category WHERE name = '_alma'); -- azonosító lekérése
UPDATE category SET name = concat(name, '2') WHERE category_id = @categoryID; -- felülírás
SELECT name FROM category WHERE category_id = @categoryID; -- felülírás ellenőrzése
DELETE FROM category WHERE category_id = @categoryID; -- törlés
SELECT category_id, name FROM category WHERE category_id = @categoryID; -- törlés ellenőrzése

-- roles tábla
INSERT INTO roles (role_id, authority) VALUES (null, '_GUEST'); -- beszúrás
SELECT role_id, authority FROM roles WHERE authority = '_GUEST'; -- beszúrás ellenőrzés
SET @roleID = (SELECT role_id FROM roles WHERE authority = '_GUEST'); -- azonosító lekérése
UPDATE roles SET authority = concat(authority, '2') WHERE role_id = @roleID; -- felülírás
SELECT role_id, authority FROM roles WHERE role_id = @roleID; -- felülírás ellenőrzése
DELETE FROM roles WHERE role_id = @roleID; -- törlés
SELECT role_id, authority FROM roles WHERE role_id = @roleID; -- törlés ellenőrzése

-- user tábla
INSERT INTO user (user_id, email, name, password, enabled, mfa_enabled, secret) VALUES (null, '_user@hhh.hu', 'UserUser', 'password', 0, 0, 'HHHJJJUUU'); -- beszúrás
SELECT user_id, email, name, password, enabled, mfa_enabled, secret FROM user WHERE email = '_user@hhh.hu'; -- beszúrás ellenőrzés
SET @userID = (SELECT user_id FROM user WHERE email = '_user@hhh.hu'); -- azonosító lekérése
UPDATE user SET email = concat(email, '2'), name = concat(name, '2'), password = concat(password, '2'), enabled = enabled + 1, mfa_enabled = mfa_enabled + 1, secret = concat(secret, '2') WHERE user_id = @userID; -- felülírás
SELECT user_id, email, name, password, enabled, mfa_enabled, secret FROM user WHERE user_id = @userID; -- felülírás ellenőrzése
DELETE FROM user WHERE user_id = @userID; -- törlés
SELECT user_id, email, name, password, enabled, mfa_enabled, secret FROM user WHERE user_id = @userID; -- törlés ellenőrzése

-- user_role_junction tábla
INSERT INTO user_role_junction (user_id, role_id) VALUES (@userID_ins, @roleID_ins); -- beszúrás
SELECT user_id, role_id FROM user_role_junction WHERE user_id = @userID_ins; -- beszúrás ellenőrzés
UPDATE user_role_junction SET role_id = @roleID_upd WHERE user_id = @userID_ins; -- felülírás
SELECT user_id, role_id FROM user_role_junction WHERE user_id = @userID_ins; -- felülírás ellenőrzése
DELETE FROM user_role_junction WHERE user_id = @userID_ins; -- törlés
SELECT user_id, role_id FROM user_role_junction WHERE user_id = @userID_ins; -- törlés ellenőrzése

-- confirmation tábla
select confirmation_id, created_date, token, user_id from confirmation;
INSERT INTO confirmation (confirmation_id, created_date, token, user_id) VALUES (null, now(), '_token', @userID_ins); -- beszúrás
SELECT confirmation_id, created_date, token, user_id FROM confirmation WHERE token = '_token'; -- beszúrás ellenőrzés
SET @confirmationID = (SELECT confirmation_id FROM confirmation WHERE token = '_token'); -- azonosító lekérése
UPDATE confirmation SET created_date = date_add(created_date, INTERVAL 1 DAY), token = concat(token, 2), user_id = @userID_upd WHERE confirmation_id = @confirmationID; -- felülírás
SELECT confirmation_id, created_date, token, user_id FROM confirmation WHERE confirmation_id = @confirmationID; -- felülírás ellenőrzése
DELETE FROM confirmation WHERE confirmation_id = @confirmationID; -- törlés
SELECT confirmation_id, created_date, token, user_id FROM confirmation WHERE confirmation_id = @confirmationID; -- törlés ellenőrzése

-- recipe tábla
INSERT INTO recipe (recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves)
			VALUES (null, now(), date_add(now(), INTERVAL 10 DAY), 'Itt következik a leírás', date_add(now(), INTERVAL 1 DAY), '_Első receptem', @categoryID_ins, @userID_ins, 1, 2, 30, 'Finom', 0); -- beszúrás
SELECT recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves FROM recipe WHERE title = '_Első receptem'; -- beszúrás ellenőrzés
SET @recipeID = (SELECT recipe_id FROM recipe WHERE title = '_Első receptem'); -- azonosító lekérése
UPDATE recipe SET	creation_at = date_add(creation_at, INTERVAL 1 DAY), 
                    deleted_at = date_add(deleted_at, INTERVAL 1 DAY),
                    description = concat(description, '2'),
                    publishing_time = date_add(publishing_time, INTERVAL 1 DAY),
                    title = concat(title, '2'),
                    category_id = @categoryID_upd,
                    user_id = @userID_upd,
                    cost = cost + 1,
                    difficulty = difficulty + 1,
                    preparation_time = preparation_time + 1,
                    subtitle = concat(subtitle, '2'),
                    number_of_saves = number_of_saves +1
		WHERE recipe_id = @recipeID; -- felülírás
SELECT recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves FROM recipe WHERE recipe_id = @recipeID; -- felülírás ellenőrzése
DELETE FROM recipe WHERE recipe_id = @recipeID; -- törlés
SELECT recipe_id, creation_at, deleted_at, description, publishing_time, title, category_id, user_id, cost, difficulty, preparation_time, subtitle, number_of_saves FROM recipe WHERE recipe_id = @recipeID; -- törlés ellenőrzése

-- recipe_ingredients tábla
INSERT INTO recipe_ingredients (recipe_recipe_id, ingredients) VALUES (@recipeID_ins, '_1 bögre valami'); -- beszúrás
SELECT recipe_recipe_id, ingredients FROM recipe_ingredients WHERE ingredients = '_1 bögre valami'; -- beszúrás ellenőrzés
UPDATE recipe_ingredients SET ingredients = concat(ingredients, '2') WHERE recipe_recipe_id = @recipeID_ins; -- felülírás
SELECT recipe_recipe_id, ingredients FROM recipe_ingredients WHERE recipe_recipe_id = @recipeID_ins; -- felülírás ellenőrzése
DELETE FROM recipe_ingredients WHERE recipe_recipe_id = @recipeID_ins; -- törlés
SELECT recipe_recipe_id, ingredients FROM recipe_ingredients WHERE recipe_recipe_id = @recipeID_ins; -- törlés ellenőrzése

-- file_registry tábla
INSERT INTO file_registry (id, category, file_path, file_size, media_type, original_file_name,upload_datetime, recipe_id, user_id) VALUES (null, 'category', 'https://res.cloudinary.com/cat.jpg', 56895, 'image/jpeg', 'macska', now(), @recipeID_ins, @userID_ins); -- beszúrás
SELECT id, category, file_path, file_size, media_type, original_file_name,upload_datetime, recipe_id, user_id FROM file_registry WHERE file_path = 'https://res.cloudinary.com/cat.jpg'; -- beszúrás ellenőrzés
SET @file_registryID = (SELECT id FROM file_registry WHERE file_path = 'https://res.cloudinary.com/cat.jpg'); -- azonosító lekérése
UPDATE file_registry SET	category = concat(category, '2'),
							file_path = concat(file_path, '2'),
                            file_size = file_size + 1,
                            media_type = concat(media_type, '2'),
                            original_file_name = concat(original_file_name, '2'),
                            upload_datetime = date_add(upload_datetime, INTERVAL 1 DAY),
                            recipe_id = @recipeID_upd,
                            user_id = @userUD_upd
		WHERE id = @file_registryID; -- felülírás
SELECT id, category, file_path, file_size, media_type, original_file_name,upload_datetime, recipe_id, user_id FROM file_registry WHERE id = @file_registryID; -- felülírás ellenőrzése
DELETE FROM file_registry WHERE id = @file_registryID; -- törlés
SELECT id, category, file_path, file_size, media_type, original_file_name,upload_datetime, recipe_id, user_id FROM file_registry WHERE id = @file_registryID; -- törlés ellenőrzése

-- ratings tábla
INSERT INTO ratings (rating_id, rating, user_id, recipe_id) VALUES (null, 3, @userID_ins, @recipeID_ins); -- beszúrás
SELECT rating_id, rating, user_id, recipe_id FROM ratings WHERE user_id = @userID_ins and recipe_id = @recipeID_ins; -- beszúrás ellenőrzés
SET @ratingID = (SELECT rating_id FROM ratings WHERE user_id = @userID_ins and recipe_id = @recipeID_ins); -- azonosító lekérése
UPDATE ratings SET	rating = rating + 1,
                    user_id = @userID_upd,
                    recipe_id = @recipeID_upd
		WHERE rating_id = @ratingID; -- felülírás
SELECT rating_id, rating, user_id, recipe_id FROM ratings WHERE rating_id = @ratingID; -- felülírás ellenőrzése
DELETE FROM ratings WHERE rating_id = @ratingID; -- törlés
SELECT rating_id, rating, user_id, recipe_id FROM ratings WHERE rating_id = @ratingID; -- törlés ellenőrzése

-- comment tábla
INSERT INTO comment (id, author, comment_body, created_at, recipe_id) VALUES (null, 'Főszakács',  '_ez egy nagyon könnyű recept.', now(), @recipeID_ins); -- beszúrás
SELECT id, author, comment_body, created_at, recipe_id FROM comment WHERE author = 'Főszakács' and comment_body = '_ez egy nagyon könnyű recept.' and recipe_id = @recipeID_ins; -- beszúrás ellenőrzés
SET @commentID = (SELECT id FROM comment WHERE author = 'Főszakács' and comment_body = '_ez egy nagyon könnyű recept.' and recipe_id = @recipeID_ins); -- azonosító lekérése
UPDATE comment SET	author = concat(author, '2'),
                    comment_body = concat(comment_body, '2'),
                    created_at = date_add(created_at, INTERVAL 1 DAY),
                    recipe_id = @recipeID_upd
		WHERE id = @commentID; -- felülírás
SELECT id, author, comment_body, created_at, recipe_id FROM comment WHERE id = @commentID; -- felülírás ellenőrzése
DELETE FROM comment WHERE id = @commentID; -- törlés
SELECT id, author, comment_body, created_at, recipe_id FROM comment WHERE id = @commentID; -- törlés ellenőrzése

-- custom_user_followed_authors tábla
INSERT INTO custom_user_followed_authors (custom_user_user_id, followed_author_names) VALUES (@userID_ins, 'Főszakács'); -- beszúrás
SELECT custom_user_user_id, followed_author_names FROM custom_user_followed_authors WHERE custom_user_user_id = @userID_ins; -- beszúrás ellenőrzés
UPDATE custom_user_followed_authors SET	followed_author_names = concat(followed_author_names, '2') WHERE custom_user_user_id = @userID_ins; -- felülírás
SELECT custom_user_user_id, followed_author_names FROM custom_user_followed_authors WHERE custom_user_user_id = @userID_ins; -- felülírás ellenőrzése
DELETE FROM custom_user_followed_authors WHERE custom_user_user_id = @userID_ins; -- törlés
SELECT custom_user_user_id, followed_author_names FROM custom_user_followed_authors WHERE custom_user_user_id = @userID_ins; -- törlés ellenőrzése

-- custom_user_followed_authors tábla
INSERT INTO custom_user_saved_recipes (custom_user_user_id, saved_recipe_id) VALUES (@userID_ins, @recipeID_ins); -- beszúrás
SELECT custom_user_user_id, saved_recipe_id FROM custom_user_saved_recipes WHERE custom_user_user_id = @userID_ins; -- beszúrás ellenőrzés
UPDATE custom_user_saved_recipes SET saved_recipe_id = @recipeID_upd WHERE custom_user_user_id = @userID_ins; -- felülírás
SELECT custom_user_user_id, saved_recipe_id FROM custom_user_saved_recipes WHERE custom_user_user_id = @userID_ins; -- felülírás ellenőrzése
DELETE FROM custom_user_saved_recipes WHERE custom_user_user_id = @userID_ins; -- törlés
SELECT custom_user_user_id, saved_recipe_id FROM custom_user_saved_recipes WHERE custom_user_user_id = @userID_ins; -- törlés ellenőrzése

-- custom_user_subscribed_users tábla
INSERT INTO custom_user_subscribed_users (custom_user_user_id, subscribed_users) VALUES (@userID_ins, 'Főszakács'); -- beszúrás
SELECT custom_user_user_id, subscribed_users FROM custom_user_subscribed_users WHERE custom_user_user_id = @userID_ins; -- beszúrás ellenőrzés
UPDATE custom_user_subscribed_users SET subscribed_users =concat(subscribed_users, '2') WHERE custom_user_user_id = @userID_ins; -- felülírás
SELECT custom_user_user_id, subscribed_users FROM custom_user_subscribed_users WHERE custom_user_user_id = @userID_ins; -- felülírás ellenőrzése
DELETE FROM custom_user_subscribed_users WHERE custom_user_user_id = @userID_ins; -- törlés
SELECT custom_user_user_id, subscribed_users FROM custom_user_subscribed_users WHERE custom_user_user_id = @userID_ins; -- törlés ellenőrzése

-- segéd rekordok törlése
DELETE FROM recipe WHERE recipe_id = @recipeID_ins;
DELETE FROM recipe WHERE recipe_id = @recipeID_upd;

DELETE FROM user WHERE user_id = @userID_ins;
DELETE FROM user WHERE user_id = @userID_upd;

DELETE FROM roles WHERE role_id = @roleID_ins;
DELETE FROM roles WHERE role_id = @roleID_upd;

DELETE FROM category WHERE category_id = @categoryID_ins;
DELETE FROM category WHERE category_id = @categoryID_upd;
