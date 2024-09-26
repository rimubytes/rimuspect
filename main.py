import asyncio
from collectors.agent import Agent
from data_pipeline.processors import DataProcessor
from storage.time_series_db import TimeSeriesDB
from query_engine.parsers import QueryParser
from api.routes import setup_routes
from visualization.graphs import GraphGenerator
from alerting.rules import AlertRuleEngine
from config_management.settings import load_config

async def main():
    config = load_config()
    agent = Agent(config['collector'])
    processor = DataProcessor()
    db = TimeSeriesDB(config['storage'])
    query_parser = QueryParser()
    alert_engine = AlertRuleEngine(config['alerting'])
    graph_generator = GraphGenerator()

    # Setup API routes
    app = setup_routes(db, query_parser, graph_generator, alert_engine)

    # Start the data collection and processing loop
    while True:
        raw_data = await agent.collect()
        processed_data = processor.process(raw_data)
        await db.store(processed_data)
        await alert_engine.check_alerts(db)
        await asyncio.sleep(config['collection_interval'])

if __name__ == "__main__":
    asyncio.run(main())