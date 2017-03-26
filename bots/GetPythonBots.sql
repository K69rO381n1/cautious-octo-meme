/*
This code takes challenge bots from the DB and writes them into files
 */

DO $$
DECLARE   bot                  RECORD;
	DECLARE num_of_bots CONSTANT INT = 100;

BEGIN
	FOR bot IN (
		SELECT
			code, filename
		FROM
			public.challenge_bots
		WHERE
			filename LIKE '%.py'
		LIMIT num_of_bots)
	LOOP
		RAISE NOTICE  'Saving % into file', bot.filename;
		PERFORM pg_catalog.pg_file_write(bot.filename, (select encode(bot.code::bytea, 'escape')), false);
	END LOOP;
END$$;
