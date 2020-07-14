import feedparser
import pyodbc 

conn = pyodbc.connect("Driver={SQL Server};"               
               "Server=your.sql.server;"
               "Database=your.database;"
               "username=your.user.name;"
               "password=your.user.password!;"
               "Trusted_Connection=yes;")
cursor = conn.cursor()

#create table dbo.rssfeeds(title nvarchar(150), link nvarchar(50), descriptionnvarchar(max))

feed = feedparser.parse("https://www.us-cert.gov/ncas/all.xml")
for entry in feed.entries:
    cursor.execute("""
    INSERT INTO dbo.rssfeeds(title,link, description)  
    VALUES (?,?,?)""",
    entry.title, entry.link, entry.description) 
    conn.commit()