import aiosqlite

class DatabaseManager:
  # CONSTRUCTOR
  def __init__(self, bot, db_path : str = "data/database.db"):
    self.bot = bot
    self.db_path = db_path
    self.conn: aiosqlite.Connection | None = None

  # Ouvre une connexion à la base de données.
  async def connect(self):
    self.conn = await aiosqlite.connect(self.db_path)
    await self.conn.execute("PRAGMA foreign_keys = ON;")

  # Clore la connexion pour éviter les conflits.
  async def close(self):
    if self.conn:
      await self.conn.close()