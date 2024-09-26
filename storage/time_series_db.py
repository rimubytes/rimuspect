import aiosqlite

class TimeSeriesDB:
    def __init__(self, config):
        self.db_path = config['db_path']

    async def store(self, data):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''
                INSERT INTO metrics (timestamp, metric_name, value)
                VALUES (?, ?, ?)
            ''', (data['timestamp'], 'cpu_percent', data['cpu_percent']))
            await db.execute('''
                INSERT INTO metrics (timestamp, metric_name, value)
                VALUES (?, ?, ?)
            ''', (data['timestamp'], 'memory_percent', data['memory_percent']))
            await db.execute('''
                INSERT INTO metrics (timestamp, metric_name, value)
                VALUES (?, ?, ?)
            ''', (data['timestamp'], 'disk_usage', data['disk_usage']))
            await db.commit()

    async def query(self, metric_name, start_time, end_time):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('''
                SELECT timestamp, value FROM metrics
                WHERE metric_name = ? AND timestamp BETWEEN ? AND ?
                ORDER BY timestamp
            ''', (metric_name, start_time, end_time)) as cursor:
                return await cursor.fetchall()
