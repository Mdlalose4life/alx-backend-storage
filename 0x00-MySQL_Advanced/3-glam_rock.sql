--  A  script that lists all bands with Glam rock as their main style, ranked by their longevity.
-- Import this table dump: metal_bands.sql.zip
-- Column names must be: band_name and lifespan
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;