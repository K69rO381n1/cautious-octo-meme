DO $$
DECLARE bot RECORD;

BEGIN
	FOR bot IN (
			SELECT 
			  code, filename
			FROM 
			  public.challenge_bots
			WHERE
			  filename LIKE '%.py'
		   )
	LOOP
		RAISE NOTICE  'Saving % into file', bot.filename;
		PERFORM pg_catalog.pg_file_write(bot.filename, (select encode(bot.code::bytea, 'escape')), false);
	END LOOP;
END$$;
