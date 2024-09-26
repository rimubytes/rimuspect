from aiohttp import web

def setup_routes(db, query_parser, graph_generator, alert_engine):
    app = web.Application()

    async def get_metric(request):
        query = request.query['q']
        parsed_query = query_parser.parse(query)
        data = await db.query(parsed_query['metric'],
                              parsed_query['start_time'],
                              parsed_query['end_time'])
        return web.json_response(data)
    
    async def get_graph(request):
        query = request.query['q']
        parsed_query = query_parser.parse(query)
        data = await db.query(parsed_query['metric'],
                              parsed_query['start_time'],
                              parsed_query['end_time'])
        graph = graph_generator.generate(data)
        return web.Response(body=graph, content_type='image/png')
    
    app.router.add_get('/app/metric', get_metric)
    app.router.add_get('/api/graph', get_graph)
    
    return app