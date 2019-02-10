from plotly import tools,offline
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

class LogsPlots():

    def __init__(self, log):
        self.log = log

    def plot_property(self, property_, h=700, w=600):

        fig = tools.make_subplots(rows=1, cols=len(self.log), shared_yaxes=False, shared_xaxes=True,
                                  subplot_titles=['Well ' + str(i) for i in range(1, len(self.log) + 1)])
        for i in range(len(self.log)):
            trace = go.Scatter(x=self.log[i][property_], y=self.log[i]['DEPTH'], )
            fig.append_trace(trace, 1, i + 1)
        fig['layout'].update(height=h, width=w, title='Well logs ' + property_)
        iplot(fig, filename='Well logs ' + property_)


    def plot_a_log(self, well_log = 1):
        most_imp_attritube_list = self.log[well_log].columns[:12]

        fig = tools.make_subplots(rows=1, cols=len(most_imp_attritube_list), shared_yaxes=True, shared_xaxes=True,
                                  subplot_titles=most_imp_attritube_list)
        for i in range(1, len(most_imp_attritube_list)):
            trace = go.Scatter(x=self.log[well_log][self.log[well_log].columns[i]], y=self.log[well_log]['DEPTH'], )
            fig.append_trace(trace, 1, i)
        fig['layout'].update(height=800, width=800, title='Well '+str(well_log))

        iplot(fig, filename='file')


class result_plots():

    def plot_3d(self, data_frame, property_):
        trace1 = go.Scatter3d(
            # df1['lat'], df1['long'], df1['DEPTH']

            x=data_frame['lat'],
            y=data_frame['long'],
            z=data_frame['DEPTH'],
            mode='markers',
            marker=dict(
                size=12,
                color=data_frame[property_],  # set color to an array/list of desired values
                colorscale='Viridis',  # choose a colorscale
                opacity=0.8,
                colorbar=dict(thickness=20)
            )
        )
        data = [trace1]
        layout = go.Layout(
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0,
            )
        )
        fig = go.Figure(data=data, layout=layout)
        iplot(fig, filename='3d grid')

    def compare_prediction(self,true,pred,property_):
        trace0 = go.Scatter(
            x=true[property_],
            y=true['DEPTH'],
            mode='lines',
            name='True Values'
        )
        trace1 = go.Scatter(
            x= pred[property_],
            y= true['DEPTH'],
            mode='lines',
            name='Predicted Values'
        )
        layout = go.Layout(
            autosize=False,
            width=250,
            height=700,
        )
        data = [trace0, trace1]

        fig = go.Figure(data=data, layout=layout)
        iplot(fig, filename=' Actual Vs Predicted ')

