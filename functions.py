import pandas as pd
from supabase import create_client, Client
import datetime
import numpy as np
import pytz

url: str = "https://geghwzramcdyqmnziwwf.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdlZ2h3enJhbWNkeXFtbnppd3dmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA4NDg1NDksImV4cCI6MjAxNjQyNDU0OX0.S_SmrTeOIEJgkdGVpNVcQpF6O9hZ61pdaDXiTk_x-wo"
supabase: Client = create_client(url, key)
user = supabase.auth.sign_in_with_password({ "email": "viniciusghora@gmail.com", "password": "182753tD#" })

holiday = [ '2001-01-01',	'2001-02-26',	'2001-02-27',	'2001-04-13',	'2001-04-21',	'2001-05-01',	'2001-06-14',	'2001-09-07',	'2001-10-12',	'2001-11-02',	'2001-11-15',	'2001-12-25',	'2002-01-01',	'2002-02-11',	'2002-02-12',	'2002-03-29',	'2002-04-21',	'2002-05-01',	'2002-05-30',	'2002-09-07',	'2002-10-12',	'2002-11-02',	'2002-11-15',	'2002-12-25',	'2003-01-01',	'2003-03-03',	'2003-03-04',	'2003-04-18',	'2003-04-21',	'2003-05-01',	'2003-06-19',	'2003-09-07',	'2003-10-12',	'2003-11-02',	'2003-11-15',	'2003-12-25',	'2004-01-01',	'2004-02-23',	'2004-02-24',	'2004-04-09',	'2004-04-21',	'2004-05-01',	'2004-06-10',	'2004-09-07',	'2004-10-12',	'2004-11-02',	'2004-11-15',	'2004-12-25',	'2005-01-01',	'2005-02-07',	'2005-02-08',	'2005-03-25',	'2005-04-21',	'2005-05-01',	'2005-05-26',	'2005-09-07',	'2005-10-12',	'2005-11-02',	'2005-11-15',	'2005-12-25',	'2006-01-01',	'2006-02-27',	'2006-02-28',	'2006-04-14',	'2006-04-21',	'2006-05-01',	'2006-06-15',	'2006-09-07',	'2006-10-12',	'2006-11-02',	'2006-11-15',	'2006-12-25',	'2007-01-01',	'2007-02-19',	'2007-02-20',	'2007-04-06',	'2007-04-21',	'2007-05-01',	'2007-06-07',	'2007-09-07',	'2007-10-12',	'2007-11-02',	'2007-11-15',	'2007-12-25',	'2008-01-01',	'2008-02-04',	'2008-02-05',	'2008-03-21',	'2008-04-21',	'2008-05-01',	'2008-05-22',	'2008-09-07',	'2008-10-12',	'2008-11-02',	'2008-11-15',	'2008-12-25',	'2009-01-01',	'2009-02-23',	'2009-02-24',	'2009-04-10',	'2009-04-21',	'2009-05-01',	'2009-06-11',	'2009-09-07',	'2009-10-12',	'2009-11-02',	'2009-11-15',	'2009-12-25',	'2010-01-01',	'2010-02-15',	'2010-02-16',	'2010-04-02',	'2010-04-21',	'2010-05-01',	'2010-06-03',	'2010-09-07',	'2010-10-12',	'2010-11-02',	'2010-11-15',	'2010-12-25',	'2011-01-01',	'2011-03-07',	'2011-03-08',	'2011-04-21',	'2011-04-22',	'2011-05-01',	'2011-06-23',	'2011-09-07',	'2011-10-12',	'2011-11-02',	'2011-11-15',	'2011-12-25',	'2012-01-01',	'2012-02-20',	'2012-02-21',	'2012-04-06',	'2012-04-21',	'2012-05-01',	'2012-06-07',	'2012-09-07',	'2012-10-12',	'2012-11-02',	'2012-11-15',	'2012-12-25',	'2013-01-01',	'2013-02-11',	'2013-02-12',	'2013-03-29',	'2013-04-21',	'2013-05-01',	'2013-05-30',	'2013-09-07',	'2013-10-12',	'2013-11-02',	'2013-11-15',	'2013-12-25',	'2014-01-01',	'2014-03-03',	'2014-03-04',	'2014-04-18',	'2014-04-21',	'2014-05-01',	'2014-06-19',	'2014-09-07',	'2014-10-12',	'2014-11-02',	'2014-11-15',	'2014-12-25',	'2015-01-01',	'2015-02-16',	'2015-02-17',	'2015-04-03',	'2015-04-21',	'2015-05-01',	'2015-06-04',	'2015-09-07',	'2015-10-12',	'2015-11-02',	'2015-11-15',	'2015-12-25',	'2016-01-01',	'2016-02-08',	'2016-02-09',	'2016-03-25',	'2016-04-21',	'2016-05-01',	'2016-05-26',	'2016-09-07',	'2016-10-12',	'2016-11-02',	'2016-11-15',	'2016-12-25',	'2017-01-01',	'2017-02-27',	'2017-02-28',	'2017-04-14',	'2017-04-21',	'2017-05-01',	'2017-06-15',
'2017-09-07',	'2017-10-12',	'2017-11-02',	'2017-11-15',	'2017-12-25',	'2018-01-01',	'2018-02-12',	'2018-02-13',	'2018-03-30',	'2018-04-21',	'2018-05-01',	'2018-05-31',	'2018-09-07',	'2018-10-12',	'2018-11-02',	'2018-11-15',	'2018-12-25',	'2019-01-01',	'2019-03-04',	'2019-03-05',	'2019-04-19',	'2019-04-21',	'2019-05-01',	'2019-06-20',	'2019-09-07',	'2019-10-12',	'2019-11-02',	'2019-11-15',	'2019-12-25',	'2020-01-01',	'2020-02-24',	'2020-02-25',	'2020-04-10',	'2020-04-21',	'2020-05-01',	'2020-06-11',	'2020-09-07',	'2020-10-12',	'2020-11-02',	'2020-11-15',	'2020-12-25',	'2021-01-01',	'2021-02-15',	'2021-02-16',	'2021-04-02',	'2021-04-21',	'2021-05-01',	'2021-06-03',	'2021-09-07',	'2021-10-12',	'2021-11-02',	'2021-11-15',	'2021-12-25',	'2022-01-01',	'2022-02-28',	'2022-03-01',	'2022-04-15',	'2022-04-21',	'2022-05-01',	'2022-06-16',	'2022-09-07',	'2022-10-12',	'2022-11-02',	'2022-11-15',	'2022-12-25',	'2023-01-01',	'2023-02-20',	'2023-02-21',	'2023-04-07',	'2023-04-21',	'2023-05-01',	'2023-06-08',	'2023-09-07',	'2023-10-12',	'2023-11-02',	'2023-11-15',	'2023-12-25',	'2024-01-01',	'2024-02-12',	'2024-02-13',	'2024-03-29',	'2024-04-21',	'2024-05-01',	'2024-05-30',	'2024-09-07',	'2024-10-12',	'2024-11-02',	'2024-11-15',	'2024-12-25',	'2025-01-01',	'2025-03-03',	'2025-03-04',	'2025-04-18',	'2025-04-21',	'2025-05-01',	'2025-06-19',	'2025-09-07',	'2025-10-12',	'2025-11-02',	'2025-11-15',	'2025-12-25',	'2026-01-01',	'2026-02-16',	'2026-02-17',	'2026-04-03',	'2026-04-21',	'2026-05-01',	'2026-06-04',	'2026-09-07',	'2026-10-12',	'2026-11-02',	'2026-11-15',	'2026-12-25',	'2027-01-01',	'2027-02-08',	'2027-02-09',	'2027-03-26',	'2027-04-21',	'2027-05-01',	'2027-05-27',	'2027-09-07',	'2027-10-12',	'2027-11-02',	'2027-11-15',	'2027-12-25',	'2028-01-01',	'2028-02-28',	'2028-02-29',	'2028-04-14',	'2028-04-21',	'2028-05-01',	'2028-06-15',	'2028-09-07',	'2028-10-12',	'2028-11-02',	'2028-11-15',	'2028-12-25',	'2029-01-01',	'2029-02-12',	'2029-02-13',	'2029-03-30',	'2029-04-21',	'2029-05-01',	'2029-05-31',	'2029-09-07',	'2029-10-12',	'2029-11-02',	'2029-11-15',	'2029-12-25',	'2030-01-01',	'2030-03-04',	'2030-03-05',	'2030-04-19',	'2030-04-21',	'2030-05-01',	'2030-06-20',	'2030-09-07',	'2030-10-12',	'2030-11-02',	'2030-11-15',	'2030-12-25',	'2031-01-01',	'2031-02-24',	'2031-02-25',	'2031-04-11',	'2031-04-21',	'2031-05-01',	'2031-06-12',	'2031-09-07',	'2031-10-12',	'2031-11-02',	'2031-11-15',	'2031-12-25',	'2032-01-01',	'2032-02-09',	'2032-02-10',	'2032-03-26',	'2032-04-21',	'2032-05-01',	'2032-05-27',	'2032-09-07',	'2032-10-12',	'2032-11-02',	'2032-11-15',	'2032-12-25',	'2033-01-01',	'2033-02-28',	'2033-03-01',	'2033-04-15',	'2033-04-21',	'2033-05-01',	'2033-06-16',	'2033-09-07',	'2033-10-12',	'2033-11-02',	'2033-11-15',	'2033-12-25',	'2034-01-01',	'2034-02-20',	'2034-02-21',
'2034-04-07',	'2034-04-21',	'2034-05-01',	'2034-06-08',	'2034-09-07',	'2034-10-12',	'2034-11-02',	'2034-11-15',	'2034-12-25',	'2035-01-01',	'2035-02-05',	'2035-02-06',	'2035-03-23',	'2035-04-21',	'2035-05-01',	'2035-05-24',	'2035-09-07',	'2035-10-12',	'2035-11-02',	'2035-11-15',	'2035-12-25',	'2036-01-01',	'2036-02-25',	'2036-02-26',	'2036-04-11',	'2036-04-21',	'2036-05-01',	'2036-06-12',	'2036-09-07',	'2036-10-12',	'2036-11-02',	'2036-11-15',	'2036-12-25',	'2037-01-01',	'2037-02-16',	'2037-02-17',	'2037-04-03',	'2037-04-21',	'2037-05-01',	'2037-06-04',	'2037-09-07',	'2037-10-12',	'2037-11-02',	'2037-11-15',	'2037-12-25',	'2038-01-01',	'2038-03-08',	'2038-03-09',	'2038-04-21',	'2038-04-23',	'2038-05-01',	'2038-06-24',	'2038-09-07',	'2038-10-12',	'2038-11-02',	'2038-11-15',	'2038-12-25',	'2039-01-01',	'2039-02-21',	'2039-02-22',	'2039-04-08',	'2039-04-21',	'2039-05-01',	'2039-06-09',	'2039-09-07',	'2039-10-12',	'2039-11-02',	'2039-11-15',	'2039-12-25',	'2040-01-01',	'2040-02-13',	'2040-02-14',	'2040-03-30',	'2040-04-21',	'2040-05-01',	'2040-05-31',	'2040-09-07',	'2040-10-12',	'2040-11-02',	'2040-11-15',	'2040-12-25',	'2041-01-01',	'2041-03-04',	'2041-03-05',	'2041-04-19',	'2041-04-21',	'2041-05-01',	'2041-06-20',	'2041-09-07',	'2041-10-12',	'2041-11-02',	'2041-11-15',	'2041-12-25',	'2042-01-01',	'2042-02-17',	'2042-02-18',	'2042-04-04',	'2042-04-21',	'2042-05-01',	'2042-06-05',	'2042-09-07',	'2042-10-12',	'2042-11-02',	'2042-11-15',	'2042-12-25',	'2043-01-01',	'2043-02-09',	'2043-02-10',	'2043-03-27',	'2043-04-21',	'2043-05-01',	'2043-05-28',	'2043-09-07',	'2043-10-12',	'2043-11-02',	'2043-11-15',	'2043-12-25',	'2044-01-01',	'2044-02-29',	'2044-03-01',	'2044-04-15',	'2044-04-21',	'2044-05-01',	'2044-06-16',	'2044-09-07',	'2044-10-12',	'2044-11-02',	'2044-11-15',	'2044-12-25',	'2045-01-01',	'2045-02-20',	'2045-02-21',	'2045-04-07',	'2045-04-21',	'2045-05-01',	'2045-06-08',	'2045-09-07',	'2045-10-12',	'2045-11-02',	'2045-11-15',	'2045-12-25',	'2046-01-01',	'2046-02-05',	'2046-02-06',	'2046-03-23',	'2046-04-21',	'2046-05-01',	'2046-05-24',	'2046-09-07',	'2046-10-12',	'2046-11-02',	'2046-11-15',	'2046-12-25',	'2047-01-01',	'2047-02-25',	'2047-02-26',	'2047-04-12',	'2047-04-21',	'2047-05-01',	'2047-06-13',	'2047-09-07',	'2047-10-12',	'2047-11-02',	'2047-11-15',	'2047-12-25',	'2048-01-01',	'2048-02-17',	'2048-02-18',	'2048-04-03',	'2048-04-21',	'2048-05-01',	'2048-06-04',	'2048-09-07',	'2048-10-12',	'2048-11-02',	'2048-11-15',	'2048-12-25',	'2049-01-01',	'2049-03-01',	'2049-03-02',	'2049-04-16',	'2049-04-21',	'2049-05-01',	'2049-06-17',	'2049-09-07',	'2049-10-12',	'2049-11-02',	'2049-11-15',	'2049-12-25',	'2050-01-01',	'2050-02-21',	'2050-02-22',	'2050-04-08',	'2050-04-21',	'2050-05-01',	'2050-06-09',	'2050-09-07',	'2050-10-12',	'2050-11-02',	'2050-11-15',
'2050-12-25',	'2051-01-01',	'2051-02-13',	'2051-02-14',	'2051-03-31',	'2051-04-21',	'2051-05-01',	'2051-06-01',	'2051-09-07',	'2051-10-12',	'2051-11-02',	'2051-11-15',	'2051-12-25',	'2052-01-01',	'2052-03-04',	'2052-03-05',	'2052-04-19',	'2052-04-21',	'2052-05-01',	'2052-06-20',	'2052-09-07',	'2052-10-12',	'2052-11-02',	'2052-11-15',	'2052-12-25',	'2053-01-01',	'2053-02-17',	'2053-02-18',	'2053-04-04',	'2053-04-21',	'2053-05-01',	'2053-06-05',	'2053-09-07',	'2053-10-12',	'2053-11-02',	'2053-11-15',	'2053-12-25',	'2054-01-01',	'2054-02-09',	'2054-02-10',	'2054-03-27',	'2054-04-21',	'2054-05-01',	'2054-05-28',	'2054-09-07',	'2054-10-12',	'2054-11-02',	'2054-11-15',	'2054-12-25',	'2055-01-01',	'2055-03-01',	'2055-03-02',	'2055-04-16',	'2055-04-21',	'2055-05-01',	'2055-06-17',	'2055-09-07',	'2055-10-12',	'2055-11-02',	'2055-11-15',	'2055-12-25',	'2056-01-01',	'2056-02-14',	'2056-02-15',	'2056-03-31',	'2056-04-21',	'2056-05-01',	'2056-06-01',	'2056-09-07',	'2056-10-12',	'2056-11-02',	'2056-11-15',	'2056-12-25',	'2057-01-01',	'2057-03-05',	'2057-03-06',	'2057-04-20',	'2057-04-21',	'2057-05-01',	'2057-06-21',	'2057-09-07',	'2057-10-12',	'2057-11-02',	'2057-11-15',	'2057-12-25',	'2058-01-01',	'2058-02-25',	'2058-02-26',	'2058-04-12',	'2058-04-21',	'2058-05-01',	'2058-06-13',	'2058-09-07',	'2058-10-12',	'2058-11-02',	'2058-11-15',	'2058-12-25',	'2059-01-01',	'2059-02-10',	'2059-02-11',	'2059-03-28',	'2059-04-21',	'2059-05-01',	'2059-05-29',	'2059-09-07',	'2059-10-12',	'2059-11-02',	'2059-11-15',	'2059-12-25',	'2060-01-01',	'2060-03-01',	'2060-03-02',	'2060-04-16',	'2060-04-21',	'2060-05-01',	'2060-06-17',	'2060-09-07',	'2060-10-12',	'2060-11-02',	'2060-11-15',	'2060-12-25',	'2061-01-01',	'2061-02-21',	'2061-02-22',	'2061-04-08',	'2061-04-21',	'2061-05-01',	'2061-06-09',	'2061-09-07',	'2061-10-12',	'2061-11-02',	'2061-11-15',	'2061-12-25',	'2062-01-01',	'2062-02-06',	'2062-02-07',	'2062-03-24',	'2062-04-21',	'2062-05-01',	'2062-05-25',	'2062-09-07',	'2062-10-12',	'2062-11-02',	'2062-11-15',	'2062-12-25',	'2063-01-01',	'2063-02-26',	'2063-02-27',	'2063-04-13',	'2063-04-21',	'2063-05-01',	'2063-06-14',	'2063-09-07',	'2063-10-12',	'2063-11-02',	'2063-11-15',	'2063-12-25',	'2064-01-01',	'2064-02-18',	'2064-02-19',	'2064-04-04',	'2064-04-21',	'2064-05-01',	'2064-06-05',	'2064-09-07',	'2064-10-12',	'2064-11-02',	'2064-11-15',	'2064-12-25',	'2065-01-01',	'2065-02-09',	'2065-02-10',	'2065-03-27',	'2065-04-21',	'2065-05-01',	'2065-05-28',	'2065-09-07',	'2065-10-12',	'2065-11-02',	'2065-11-15',	'2065-12-25',	'2066-01-01',	'2066-02-22',	'2066-02-23',	'2066-04-09',	'2066-04-21',	'2066-05-01',	'2066-06-10',	'2066-09-07',	'2066-10-12',	'2066-11-02',	'2066-11-15',	'2066-12-25',	'2067-01-01',	'2067-02-14',	'2067-02-15',	'2067-04-01',	'2067-04-21',	'2067-05-01',	'2067-06-02',
'2067-09-07',	'2067-10-12',	'2067-11-02',	'2067-11-15',	'2067-12-25',	'2068-01-01',	'2068-03-05',	'2068-03-06',	'2068-04-20',	'2068-04-21',	'2068-05-01',	'2068-06-21',	'2068-09-07',	'2068-10-12',	'2068-11-02',	'2068-11-15',	'2068-12-25',	'2069-01-01',	'2069-02-25',	'2069-02-26',	'2069-04-12',	'2069-04-21',	'2069-05-01',	'2069-06-13',	'2069-09-07',	'2069-10-12',	'2069-11-02',	'2069-11-15',	'2069-12-25',	'2070-01-01',	'2070-02-10',	'2070-02-11',	'2070-03-28',	'2070-04-21',	'2070-05-01',	'2070-05-29',	'2070-09-07',	'2070-10-12',	'2070-11-02',	'2070-11-15',	'2070-12-25',	'2071-01-01',	'2071-03-02',	'2071-03-03',	'2071-04-17',	'2071-04-21',	'2071-05-01',	'2071-06-18',	'2071-09-07',	'2071-10-12',	'2071-11-02',	'2071-11-15',	'2071-12-25',	'2072-01-01',	'2072-02-22',	'2072-02-23',	'2072-04-08',	'2072-04-21',	'2072-05-01',	'2072-06-09',	'2072-09-07',	'2072-10-12',	'2072-11-02',	'2072-11-15',	'2072-12-25',	'2073-01-01',	'2073-02-06',	'2073-02-07',	'2073-03-24',	'2073-04-21',	'2073-05-01',	'2073-05-25',	'2073-09-07',	'2073-10-12',	'2073-11-02',	'2073-11-15',	'2073-12-25',	'2074-01-01',	'2074-02-26',	'2074-02-27',	'2074-04-13',	'2074-04-21',	'2074-05-01',	'2074-06-14',	'2074-09-07',	'2074-10-12',	'2074-11-02',	'2074-11-15',	'2074-12-25',	'2075-01-01',	'2075-02-18',	'2075-02-19',	'2075-04-05',	'2075-04-21',	'2075-05-01',	'2075-06-06',	'2075-09-07',	'2075-10-12',	'2075-11-02',	'2075-11-15',	'2075-12-25',	'2076-01-01',	'2076-03-02',	'2076-03-03',	'2076-04-17',	'2076-04-21',	'2076-05-01',	'2076-06-18',	'2076-09-07',	'2076-10-12',	'2076-11-02',	'2076-11-15',	'2076-12-25',	'2077-01-01',	'2077-02-22',	'2077-02-23',	'2077-04-09',	'2077-04-21',	'2077-05-01',	'2077-06-10',	'2077-09-07',	'2077-10-12',	'2077-11-02',	'2077-11-15',	'2077-12-25',	'2078-01-01',	'2078-02-14',	'2078-02-15',	'2078-04-01',	'2078-04-21',	'2078-05-01',	'2078-06-02',	'2078-09-07',	'2078-10-12',	'2078-11-02',	'2078-11-15',	'2078-12-25',	'2079-01-01',	'2079-03-06',	'2079-03-07',	'2079-04-21',	'2079-04-21',	'2079-05-01',	'2079-06-22',	'2079-09-07',	'2079-10-12',	'2079-11-02',	'2079-11-15',	'2079-12-25',	'2080-01-01',	'2080-02-19',	'2080-02-20',	'2080-04-05',	'2080-04-21',	'2080-05-01',	'2080-06-06',	'2080-09-07',	'2080-10-12',	'2080-11-02',	'2080-11-15',	'2080-12-25',	'2081-01-01',	'2081-02-10',	'2081-02-11',	'2081-03-28',	'2081-04-21',	'2081-05-01',	'2081-05-29',	'2081-09-07',	'2081-10-12',	'2081-11-02',	'2081-11-15',	'2081-12-25',	'2082-01-01',	'2082-03-02',	'2082-03-03',	'2082-04-17',	'2082-04-21',	'2082-05-01',	'2082-06-18',	'2082-09-07',	'2082-10-12',	'2082-11-02',	'2082-11-15',	'2082-12-25',	'2083-01-01',	'2083-02-15',	'2083-02-16',	'2083-04-02',	'2083-04-21',	'2083-05-01',	'2083-06-03',	'2083-09-07',	'2083-10-12',	'2083-11-02',	'2083-11-15',	'2083-12-25',	'2084-01-01',	'2084-02-07',	'2084-02-08',
'2084-03-24',	'2084-04-21',	'2084-05-01',	'2084-05-25',	'2084-09-07',	'2084-10-12',	'2084-11-02',	'2084-11-15',	'2084-12-25',	'2085-01-01',	'2085-02-26',	'2085-02-27',	'2085-04-13',	'2085-04-21',	'2085-05-01',	'2085-06-14',	'2085-09-07',	'2085-10-12',	'2085-11-02',	'2085-11-15',	'2085-12-25',	'2086-01-01',	'2086-02-11',	'2086-02-12',	'2086-03-29',	'2086-04-21',	'2086-05-01',	'2086-05-30',	'2086-09-07',	'2086-10-12',	'2086-11-02',	'2086-11-15',	'2086-12-25',	'2087-01-01',	'2087-03-03',	'2087-03-04',	'2087-04-18',	'2087-04-21',	'2087-05-01',	'2087-06-19',	'2087-09-07',	'2087-10-12',	'2087-11-02',	'2087-11-15',	'2087-12-25',	'2088-01-01',	'2088-02-23',	'2088-02-24',	'2088-04-09',	'2088-04-21',	'2088-05-01',	'2088-06-10',	'2088-09-07',	'2088-10-12',	'2088-11-02',	'2088-11-15',	'2088-12-25',	'2089-01-01',	'2089-02-14',	'2089-02-15',	'2089-04-01',	'2089-04-21',	'2089-05-01',	'2089-06-02',	'2089-09-07',	'2089-10-12',	'2089-11-02',	'2089-11-15',	'2089-12-25',	'2090-01-01',	'2090-02-27',	'2090-02-28',	'2090-04-14',	'2090-04-21',	'2090-05-01',	'2090-06-15',	'2090-09-07',	'2090-10-12',	'2090-11-02',	'2090-11-15',	'2090-12-25',	'2091-01-01',	'2091-02-19',	'2091-02-20',	'2091-04-06',	'2091-04-21',	'2091-05-01',	'2091-06-07',	'2091-09-07',	'2091-10-12',	'2091-11-02',	'2091-11-15',	'2091-12-25',	'2092-01-01',	'2092-02-11',	'2092-02-12',	'2092-03-28',	'2092-04-21',	'2092-05-01',	'2092-05-29',	'2092-09-07',	'2092-10-12',	'2092-11-02',	'2092-11-15',	'2092-12-25',	'2093-01-01',	'2093-02-23',	'2093-02-24',	'2093-04-10',	'2093-04-21',	'2093-05-01',	'2093-06-11',	'2093-09-07',	'2093-10-12',	'2093-11-02',	'2093-11-15',	'2093-12-25',	'2094-01-01',	'2094-02-15',	'2094-02-16',	'2094-04-02',	'2094-04-21',	'2094-05-01',	'2094-06-03',	'2094-09-07',	'2094-10-12',	'2094-11-02',	'2094-11-15',	'2094-12-25',	'2095-01-01',	'2095-03-07',	'2095-03-08',	'2095-04-21',	'2095-04-22',	'2095-05-01',	'2095-06-23',	'2095-09-07',	'2095-10-12',	'2095-11-02',	'2095-11-15',	'2095-12-25',	'2096-01-01',	'2096-02-27',	'2096-02-28',	'2096-04-13',	'2096-04-21',	'2096-05-01',	'2096-06-14',	'2096-09-07',	'2096-10-12',	'2096-11-02',	'2096-11-15',	'2096-12-25',	'2097-01-01',	'2097-02-11',	'2097-02-12',	'2097-03-29',	'2097-04-21',	'2097-05-01',	'2097-05-30',	'2097-09-07',	'2097-10-12',	'2097-11-02',	'2097-11-15',	'2097-12-25',	'2098-01-01',	'2098-03-03',	'2098-03-04',	'2098-04-18',	'2098-04-21',	'2098-05-01',	'2098-06-19',	'2098-09-07',	'2098-10-12',	'2098-11-02',	'2098-11-15',	'2098-12-25',	'2099-01-01',	'2099-02-23',	'2099-02-24',	'2099-04-10',	'2099-04-21',	'2099-05-01',	'2099-06-11',	'2099-09-07',	'2099-10-12',	'2099-11-02',	'2099-11-15',	'2099-12-25' ]

# NTN-B
def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

def get_ipca_index_base():
  data_base = supabase.table("ipca_data").select("*").eq("year", 2000).eq("month", "JUN").execute()
  ipca_index_base = data_base.data[0]['index']
  return ipca_index_base

def parse_month(month):
  month_dict = {"1": "JAN", "2": "FEV", "3": "MAR", "4": "ABR", "5": "MAI", "6": "JUN", "7": "JUL", "8": "AGO", "9": "SET", "10": "OUT", "11": "NOV", "12": "DEZ"}
  return month_dict[month]

def get_ipca(month, year):
  ipca = supabase.table("ipca_data").select("*").eq("year", int(year)).eq("month", parse_month(str(int(month)))).execute()
  return ipca.data[0]['index']

def calc_vna_15(data):
  month = int(data[3:5])
  year = int(data[6:])
  ipca_index_actual = get_ipca(month - 1, year)
  ipca_index_base = get_ipca_index_base()
  vna = (ipca_index_actual/ipca_index_base) * 1000
  return truncate_float(vna, 6)

def calc_vna_past(month, year):
  ipca_index = get_ipca(month, year)
  ipca_index_base = get_ipca_index_base()
  vna = (ipca_index/ipca_index_base) * 1000
  return truncate_float(vna, 6)

# VNA CALCULO
def get_t_minus_1_date(data):
  day =  int(data[0:2])
  month = int(data[3:5])
  year = int(data[6:])
  date = datetime.date(year, month, day)
  if (month == 1):
    return {"month": 12, "year": year - 1}
  return {"month": str(month - 1), "year": str(year)}

def get_t_minus_2_date(data):
  month = int(data[3:5])
  year = int(data[6:])
  if (month == 1):
    return {"month": str(11), "year": str(year - 1)}
  elif (month == 2):
    return {"month": 12, "year": year - 1}
  return {"month": str(month - 2), "year": str(year)}

def add_1_month(data):
  if (data.month == 12):
    return datetime.date(data.year + 1, 1, 15)
  return datetime.date(data.year, data.month + 1, 15)

def add_1_month_ntnc(data):
  if (data.month == 12):
    return datetime.date(data.year + 1, 1, 1)
  return datetime.date(data.year, data.month + 1, 1)

def get_last_ipca_expectation_avaliabe(data):
  day =  int(data[0:2])
  month = int(data[3:5])
  year = int(data[6:])
  data_lte = str(year) + "-" + str(month) + "-" + str(day)
  ipca_expec = supabase.table("ipca_expec").select("*").eq("avaliable", True).lte('validate_date', data_lte).order('validate_date', desc=True).limit(1).execute()
  return ipca_expec

def verify_next_busday(pay_day):
  verify_date = datetime.datetime.strptime(pay_day, "%d/%m/%Y")
  busday = False
  while busday == False:
    verify_holiday_date = verify_date.strftime("%Y-%m-%d")
    if verify_holiday_date in holiday:
      verify_date += datetime.timedelta(days=1)
      continue
    if verify_date.weekday() == 5:
      verify_date += datetime.timedelta(days=2)
      continue
    if verify_date.weekday() == 6:
      verify_date += datetime.timedelta(days=1)
      continue
    busday = True
  return verify_date.date()

def verify_next_busday_datetime(pay_day):
  verify_date = datetime.datetime.strptime(pay_day, "%d/%m/%Y")
  busday = False
  while busday == False:
    verify_holiday_date = verify_date.strftime("%Y-%m-%d")
    if verify_holiday_date in holiday:
      verify_date += datetime.timedelta(days=1)
      continue
    if verify_date.weekday() == 5:
      verify_date += datetime.timedelta(days=2)
      continue
    if verify_date.weekday() == 6:
      verify_date += datetime.timedelta(days=1)
      continue
    busday = True
  return verify_date

def verify_busday(date):
  if date.weekday() == 5 or date.weekday() == 6:
    day = verify_next_busday_datetime(date.strftime("%d/%m/%Y"))
    return day
  if date.strftime("%Y-%m-%d") in holiday:
    day = verify_next_busday_datetime(date.strftime("%d/%m/%Y"))
    return day
  return date

def calc_n_cupons(selected_date, vencimento_titulo):

  # vencimento 05
  if vencimento_titulo.month == 5:
    n_cupons = (vencimento_titulo.year - selected_date.year) * 2
    if selected_date.month < 5:
      n_cupons += 2
    if selected_date.month > 5 and selected_date.month < 11:
      n_cupons += 1
    if selected_date.month == 5 and selected_date.date() < verify_next_busday(f"15/05/{str(selected_date.year)}"):
      n_cupons += 2
    if selected_date.month == 5 and selected_date.date() >= verify_next_busday(f"15/05/{str(selected_date.year)}"):
      n_cupons += 1
    if selected_date.month == 11 and selected_date.date() < verify_next_busday(f"15/11/{str(selected_date.year)}"):
      n_cupons += 1
    if selected_date.month == 11 and selected_date.date() >= verify_next_busday(f"15/11/{str(selected_date.year)}"):
      n_cupons -= 1
    if selected_date.month > 11:
      n_cupons += 1

  # Vencimento mês 08
  if vencimento_titulo.month == 8:
    n_cupons = (vencimento_titulo.year - selected_date.year) * 2
    if selected_date.month < 2:
      n_cupons += 2
    if selected_date.month > 2 and selected_date.month < 8:
      n_cupons += 1
    if selected_date.month == 2 and selected_date.date() < verify_next_busday(f"15/02/{str(selected_date.year)}"):
      n_cupons += 2
    if selected_date.month == 2 and selected_date.date() >= verify_next_busday(f"15/02/{str(selected_date.year)}"):
      n_cupons += 1
    if selected_date.month == 8 and selected_date.date() < verify_next_busday(f"15/08/{str(selected_date.year)}"):
      n_cupons += 1
    if selected_date.month == 8 and selected_date.date() >= verify_next_busday(f"15/08/{str(selected_date.year)}"):
      n_cupons = n_cupons
    if selected_date.month > 8:
      n_cupons += 1

  if vencimento_titulo.month == 1:
    n_cupons = (vencimento_titulo.year - selected_date.year) * 2
    n_cupons += 2

  return n_cupons

def calc_next_cupom_payment_day(start_date, month_validate):

  if month_validate == 8:
    if start_date.month < 2:
      new_date = datetime.date(start_date.year, 2, 15)
      return new_date
    if start_date.month == 2 and start_date.day < 15:
      new_date = datetime.date(start_date.year, 2, 15)
      return new_date
    if start_date.month == 2 and start_date.day >= 15:
      new_date = datetime.date(start_date.year, 8, 15)
      return new_date
    if start_date.month > 2 and start_date.month < 8:
      new_date = datetime.date(start_date.year, 8, 15)
      return new_date
    if start_date.month == 8 and start_date.day < 15:
      new_date = datetime.date(start_date.year, 8, 15)
      return new_date
    if start_date.month == 8 and start_date.day >= 15:
      new_date = datetime.date(int(start_date.year) + 1, 2, 15)
      return new_date
    if start_date.month > 8:
      new_date = datetime.date(start_date.year + 1, 2, 15)
      return new_date

  if month_validate == 5:
    if start_date.month < 5:
      new_date = datetime.date(start_date.year, 5, 15)
      return new_date
    if start_date.month == 5 and start_date.day < 15:
      new_date = datetime.date(start_date.year, 5, 15)
      return new_date
    if start_date.month == 5 and start_date.day >= 15:
      new_date = datetime.date(start_date.year, 11, 15)
      return new_date
    if start_date.month > 5 and start_date.month < 11:
      new_date = datetime.date(start_date.year, 11, 15)
      return new_date
    if start_date.month == 11 and start_date.day < 15:
      new_date = datetime.date(start_date.year, 11, 15)
      return new_date
    if start_date.month == 11 and start_date.day >= 15:
      new_date = datetime.date(int(start_date.year) + 1, 5, 15)
      return new_date
    if start_date.month > 11:
      new_date = datetime.date(start_date.year + 1, 5, 15)
      return new_date

  if month_validate == 1:
    if start_date.month == 1 and start_date.day >= 1:
      new_date = datetime.date(start_date.year, 7, 1)
      return new_date
    if start_date.month > 1 and start_date.month < 7:
      new_date = datetime.date(start_date.year, 7, 1)
      return new_date
    if start_date.month == 7 and start_date.day >= 1:
      new_date = datetime.date(int(start_date.year) + 1, 1, 1)
      return new_date
    if start_date.month > 7:
      new_date = datetime.date(int(start_date.year) + 1, 1, 1)
      return new_date
    
def get_pu(vna, selected_date, due_date, taxa):
  cotacao = 0
  verify_cupom_date = selected_date
  for n_cupom in range(calc_n_cupons(selected_date,due_date)):
    next_pay = calc_next_cupom_payment_day(verify_cupom_date, due_date.month)
    verify_cupom_date = verify_next_busday(next_pay.strftime("%d/%m/%Y"))
    if (verify_cupom_date <= due_date.date()):
      du_i = np.busday_count(selected_date.date(), verify_cupom_date, holidays=holiday)
      cotacao += (((1 + 0.06) ** 0.5) - 1) / ((1 + taxa) ** (du_i/252))
    else:
      break

  du_n = np.busday_count(selected_date.date(), due_date.date(), holidays=holiday)
  cotacao = cotacao + (1 / ((1 + taxa) ** (du_n/252)))
  cotacao = truncate_float(cotacao, 6)
  pu = cotacao * vna
  pu = truncate_float(pu, 6)
  return pu

def get_ipca_data_avaliabe(month, year):
  try:
    ipca_data = supabase.table("ipca_data").select("*").eq('year', year).eq('month', parse_month(month)).execute()
    ipca_data = ipca_data.data[0]
    return ipca_data
  except:
    return False

def get_last_ipca_avaliable():
    ipca_data = supabase.table("ipca_data").select("*").order('avaliable_date', desc=True).not_.is_('avaliable_date', 'null').limit(1).execute()
    ipca_data = ipca_data.data[0]
    return ipca_data

def get_vna(selected_date):
  try:
    last_expec = get_last_ipca_expectation_avaliabe(selected_date.strftime("%d/%m/%Y"))
    date_validate_expec = last_expec.data[0]['validate_date']
    validate_date = datetime.date(int(date_validate_expec[0:4]), int(date_validate_expec[5:7]), int(date_validate_expec[8:])) if date_validate_expec else False
  except:
    last_expec = False
    date_validate_expec = False
    validate_date = False

  t1 = get_t_minus_1_date(selected_date.strftime("%d/%m/%Y"))
  t2 = get_t_minus_2_date(selected_date.strftime("%d/%m/%Y"))

  ipca_avaliable = get_ipca_data_avaliabe(t1['month'], t1['year'])
  now = datetime.datetime.now()


  # CASO III - data selecionada > data que saiu o IPCA do último mês e Data selecionada < dia 15
  if selected_date.day < 15 and ipca_avaliable:
    ipca_data_avaliable = datetime.datetime.strptime(ipca_avaliable['avaliable_date'], "%Y-%m-%d")
    if selected_date.date() >= ipca_data_avaliable.date():
      t1 = get_t_minus_1_date(selected_date.strftime("%d/%m/%Y"))
      t2 = get_t_minus_2_date(selected_date.strftime("%d/%m/%Y"))
      ipca_t1 = get_ipca(t1["month"], t1["year"])
      ipca_t2 = get_ipca(t2["month"], t2["year"])
      vna_minus_1 = calc_vna_past(t2['month'], t2['year'])
      start = datetime.date(int(t1["year"]), int(t1["month"]), 15)
      du1 = np.busday_count(start, selected_date.date(), holidays=holiday)
      selected_date_15 = datetime.date(selected_date.year, selected_date.month, 15)
      du2 = np.busday_count(start, selected_date_15, holidays=holiday)
      vna = vna_minus_1 * ((ipca_t1/ipca_t2) ** (du1/du2))
      vna = truncate_float(vna, 6)
      return vna

  # CASO II - Data selecionada >= dia 15 e data selecionada < dia de validade do primeiro IPCA Projetado
  if selected_date.day >= 15 and validate_date and selected_date.day < validate_date.day:
    vna = calc_vna_15(selected_date.strftime("%d/%m/%Y"))
    return vna

  # CASO I - Data selecionada >= dia de início de validade do primeiro IPCA e Não saiu o IPCA do próximo mês
  if validate_date:
      t1 = get_t_minus_1_date(validate_date.strftime("%d/%m/%Y"))
      t2 = get_t_minus_2_date(validate_date.strftime("%d/%m/%Y"))
      last_ipca = get_last_ipca_avaliable()
      get_base_ipca = get_ipca_index_base()
      vna_minus_1 = (last_ipca['index']/get_base_ipca)*1000
      vna_minus_1 = truncate_float(vna_minus_1, 6)
      last_expec_ipca = last_expec.data[0]['projection']
      start = datetime.datetime.strptime(last_ipca['avaliable_date'], "%Y-%m-%d")
      start = datetime.date(int(start.year), int(start.month), 15)
      du1 = np.busday_count(start, selected_date.date(), holidays=holiday)
      if selected_date.month == start.month:
        end = add_1_month(selected_date)
      else:
        end = datetime.date(int(selected_date.year), int(selected_date.month), 15)
      du2 = np.busday_count(start, end, holidays=holiday)
      vna = vna_minus_1 * ((1 + (float(last_expec_ipca) * 0.01)) ** (du1/du2))
      vna = truncate_float(vna, 6)
      return vna

def get_pu_ltn(taxa, start_date, due_date):
  du = np.busday_count(start_date.date(), due_date.date(), holidays=holiday)
  pu = 1000 / ((1 + taxa) ** (du/252))
  return truncate_float(pu, 6)

def get_tax_ltn(pu, start_date, due_date):
  du = np.busday_count(start_date.date(), due_date.date(), holidays=holiday)
  taxa = ((1000/pu) ** (252/du) - 1) * 100
  return truncate_float(taxa, 3)

def get_pu_ntnf(selected_date, due_date, taxa):
  pu = 0
  verify_cupom_date = selected_date
  for n_cupom in range(calc_n_cupons(selected_date,due_date)):
    next_pay = calc_next_cupom_payment_day(verify_cupom_date, due_date.month)
    verify_cupom_date = verify_next_busday(next_pay.strftime("%d/%m/%Y"))
    if (verify_cupom_date <= due_date.date()):
      du_i = np.busday_count(selected_date.date(), verify_cupom_date, holidays=holiday)
      pu += ((((1 + 0.1) ** 0.5) - 1) * 1000) / ((1 + taxa) ** (du_i/252))
    else:
      break

  du_n = np.busday_count(selected_date.date(), due_date.date(), holidays=holiday)
  pu = pu + (1000 / ((1 + taxa) ** (du_n/252)))
  pu = truncate_float(pu, 6)
  return pu

def get_fator_selic(selected_date):
  data = str(selected_date.year) + "-" + str(selected_date.month) + "-" + str(selected_date.day)
  ipca_expec = supabase.table("selic_factor").select("*").eq("date", data).limit(1).execute()
  return ipca_expec.data[0]['selic_factor']

def get_vna_lft(selected_date):
  fator_selic = get_fator_selic(selected_date)
  vna = 1000 * fator_selic
  return truncate_float(vna, 6)

def get_pu_lft(vna, selected_date, due_date, taxa):
  taxa = taxa
  du_n = np.busday_count(selected_date.date(), due_date.date(), holidays=holiday)
  pu = (1 / ((taxa + 1) ** (du_n/252))) * vna
  return truncate_float(pu, 6)

def get_igpm_index_base():
  data_base = supabase.table("igpm_data").select("*").eq("year", 2000).eq("month", "JUN").execute()
  igm_index_base = data_base.data[0]['index']
  return igm_index_base

def get_igpm_index(year, month):
  igpm = supabase.table("igpm_data").select("*").eq("year", int(year)).eq("month", parse_month(str(int(month)))).execute()
  return igpm.data[0]['index']

def get_igpm_avaliable_date(date):
  try:
    igpm = supabase.table("igpm_data").select("*").eq("year", int(date.year)).eq("month", parse_month(str(int(date.month)))).execute()
    igpm_data = igpm.data[0]['avaliable_date']
    avaliable_data = datetime.datetime.strptime(igpm_data, "%Y-%m-%d")
    return avaliable_data
  except:
    return False

def calc_vna_day_1(selected_date):
  t_1 = get_t_minus_1_date(selected_date.strftime("%d/%m/%Y"))
  igpm_t_1 = get_igpm_index(t_1['year'], t_1['month'])
  igpm_base = get_igpm_index_base()
  vna = (igpm_t_1/igpm_base) * 1000
  return truncate_float(vna, 6)

def get_last_igpm_expectation_avaliabe(data):
  day =  int(data[0:2])
  month = int(data[3:5])
  year = int(data[6:])
  data_lte = str(year) + "-" + str(month) + "-" + str(day)
  ipca_expec = supabase.table("igpm_expec").select("*").eq("avaliable", True).lte('validate_date', data_lte).order('validate_date', desc=True).limit(1).execute()
  return ipca_expec.data[0]['projection']

def get_vna_igpm(selected_date):
  igpm_avaliable_date = get_igpm_avaliable_date(selected_date)

  # (I) - Primeiro dia do mês
  if selected_date.day == 1:
    vna = calc_vna_day_1(selected_date)
    return vna

  # (II) - Cenário após a divulgação do IGMP e o dia primeiro do mês seguinte. Ex: Entre o dia 29/11 (Data de divulgação do IGMP do mês de novembro) até antes do dia 01/12
  if igpm_avaliable_date and selected_date.date() >= igpm_avaliable_date.date():
    t_1 = get_t_minus_1_date(selected_date.strftime("%d/%m/%Y"))
    igpm_t = get_igpm_index(selected_date.year, selected_date.month)
    igpm_t_1 = get_igpm_index(t_1['year'], t_1['month'])
    first_day = datetime.datetime(selected_date.year, selected_date.month, 1)
    du_1 = np.busday_count(first_day.date(), selected_date.date(), holidays=holiday)
    end_date = add_1_month_ntnc(selected_date)
    du_2 = np.busday_count(first_day.date(), end_date, holidays=holiday)
    igpm_base = get_igpm_index_base()
    vna_t_minus_1 = (igpm_t_1/igpm_base) * 1000
    vna_t_minus_1 = truncate_float(vna_t_minus_1, 6)
    vna = ((igpm_t/igpm_t_1) ** (du_1/du_2)) * vna_t_minus_1
    return truncate_float(vna, 6)

  # (III) - Após o primeiro dia do mês, até a saída do IGMP do mês.
  if selected_date.day > 1:
    if igpm_avaliable_date:
      if selected_date.date() < igpm_avaliable_date.date():
        vna_t_minus_1 = calc_vna_day_1(selected_date)
        igpm_proj = get_last_igpm_expectation_avaliabe(selected_date.strftime("%d/%m/%Y"))
        first_day = datetime.datetime(selected_date.year, selected_date.month, 1)
        du_1 = np.busday_count(first_day.date(), selected_date.date(), holidays=holiday)
        end_date = add_1_month_ntnc(selected_date)
        du_2 = np.busday_count(first_day.date(), end_date, holidays=holiday)
        vna = ((1 + (igpm_proj * 0.01)) ** (du_1/du_2)) * vna_t_minus_1
        return truncate_float(vna, 6)
    else:
      vna_t_minus_1 = calc_vna_day_1(selected_date)
      igpm_proj = get_last_igpm_expectation_avaliabe(selected_date.strftime("%d/%m/%Y"))
      first_day = datetime.datetime(selected_date.year, selected_date.month, 1)
      du_1 = np.busday_count(first_day.date(), selected_date.date(), holidays=holiday)
      end_date = add_1_month_ntnc(selected_date)
      du_2 = np.busday_count(first_day.date(), end_date, holidays=holiday)
      vna = ((1 + (igpm_proj * 0.01)) ** (du_1/du_2)) * vna_t_minus_1
      return truncate_float(vna, 6)

def get_pu_ntn_c(vna, selected_date, due_date, taxa):
  cotacao = 0
  verify_cupom_date = selected_date
  for n_cupom in range(calc_n_cupons(selected_date,due_date)):
    next_pay = calc_next_cupom_payment_day(verify_cupom_date, due_date.month)
    verify_cupom_date = verify_next_busday(next_pay.strftime("%d/%m/%Y"))
    if (verify_cupom_date <= due_date.date()):
      du_i = np.busday_count(selected_date.date(), verify_cupom_date, holidays=holiday)
      cotacao += (((1 + 0.12) ** 0.5) - 1) / ((1 + taxa) ** (du_i/252))
    else:
      break

  du_n = np.busday_count(selected_date.date(), due_date.date(), holidays=holiday)
  cotacao = cotacao + (1 / ((1 + taxa) ** (du_n/252)))
  cotacao = truncate_float(cotacao, 6)
  pu = cotacao * vna
  pu = truncate_float(pu, 6)
  return pu

