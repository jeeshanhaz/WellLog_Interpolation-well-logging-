import numpy as np
import pandas as pd
import folium

class LoadDataset:
    def __init__(self, log=[], well_number_in_m = 1):
        self.log = log
        self.well_number_in_m = well_number_in_m
        # self.map_lat =map_lat
        # self.map_long = map_long
        # self.m = folium.Map(
        #     location=[self.map_long, self.map_long],
        #     zoom_start=12,
        #     tiles='Stamen Terrain'
        # )
        # folium.LayerControl().add_to(self.m)

    def latlong_to_cartian(self, x):
        for i in range(len(x['lat'])):
            x['lat'][i], x['long'][i] = self.cartesian(x['lat'][i], x['long'][i])
        return x['lat'], x['long']


    def add_well(self, path, lat_, long_):
        data = pd.read_csv(path)
        data['lat'] = lat_
        data['long'] = long_
        data = data.replace(-999.25, np.nan)
        # data['lat'], data['long'] = self.latlong_to_cartian(data)        **** Temporary halted ****
        self.log.append(data)

        if(self.well_number_in_m==1):
            self.m = folium.Map(
                location=[lat_, long_],
                zoom_start=12,
                tiles='Stamen Terrain'
            )
            folium.LayerControl().add_to(self.m)

        folium.Marker([lat_,long_], popup='<i>Well </i>' + str(self.well_number_in_m) + '   ( '+str(lat_)+','+str(long_)
                                          +' )').add_to(self.m)
        self.well_number_in_m = self.well_number_in_m+1
        return self.log,self.m

    def cartesian(self, lat, lon):
        lat = np.radians(lat)
        lon = np.radians(lon)
        R = 6371.0
        x = R * np.cos(lat) * np.cos(lon)
        y = R * np.cos(lat) * np.sin(lon)
        return x, y


    def height_adjustment(self):
        print(' Height Adjustment for each well ')
        new_log = []
        top_layers = []
        bottom_layers = []
        mini_diff = 1000
        for i in range(len(self.log)):
            print('\n\n LOG NUMBER : ' + str(i))
            h1 = int(input('\n Top Layer : '))
            h2 = int(input(' Bottom Layer : '))

            top_layers.append(h1)
            bottom_layers.append(h2)

            mini_diff = min(mini_diff,h2-h1)


            # self.top_height = max(self.top_height,h1)
            # self.bottom_height = min(self.bottom_height,h2)

            # new_log.append(new_log[i][new_log[i]['DEPTH'] >= h2])
        for i in range(len(self.log)):
            new_log.append(self.log[i].loc[(self.log[i]['DEPTH'] >= top_layers[i]) &
                                           (self.log[i]['DEPTH'] <= (top_layers[i]+mini_diff))])
        return new_log





