import matplotlib.pyplot as plt
import io

class GraphGenerator:
    def generate(self, data):
        timestamps, values = zip(*data)
        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, values)
        plt.title('Metric Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf.getvalue()
