from dateutil import relativedelta
import datetime
from firebase import firebase

class ServiceAPI:
    base_url_service = 'https://shiftstestapi.firebaseio.com/'

    def list_location(self, locationdId = None):
        if (locationdId is None):
            f = firebase.FirebaseApplication(self.base_url_service, None)
            return f.get('/locations/', None)
        else:
            f = firebase.FirebaseApplication(self.base_url_service, None)
            return f.get('/locations/'+str(locationdId), None)

    def list_users_by_location(self, location):
        f = firebase.FirebaseApplication(self.base_url_service, None)
        return f.get("/users/"+str(location), None)

    def get_user_by_id(self, userId):
        f = firebase.FirebaseApplication(self.base_url_service, None)
        return f.get('/users/', userId)

    def get_time_punches(self, user_id):
        f = firebase.FirebaseApplication(self.base_url_service, None)
        return f.get('/timePunches/', None, params={'userId': user_id})

    def _format_str_to_date(self, str_to_date):
        print("date = "+str_to_date)
        try:
            return datetime.datetime.strptime(str_to_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
        raise ValueError('no valid date format found')


    def _calc_shift_hours(self, shift_start, shift_end, hourlywage=0):
        '''calculate total time worked in a day'''

        if shift_start == "0000-00-00 00:00:00" or shift_end == "0000-00-00 00:00:00":
            return 0

        dt1 = self._format_str_to_date(shift_start)
        dt2 = self._format_str_to_date(shift_end)
        worked_hours = relativedelta.relativedelta(dt2, dt1)
        return worked_hours.hours

    def processing_time_punches(self, user_id):
        total_hours_worked = 0
        overtime_worked = 100
        times_punches = self.get_time_punches(user_id)
        #print(times_punches)
        for (key, value) in times_punches.items():
            hourlywage = value['hourlyWage']
            clockedIn = value['clockedIn']
            clokedOut = value['clockedOut']
            total_hours_worked += self._calc_shift_hours(clockedIn, clokedOut)

        result = {'total_hours': total_hours_worked,
                  'overtime': overtime_worked}
        return result

    def get_users_data(self, locationId):
        data_users = self.list_users_by_location(locationId)
        result = []

        for (key, value) in data_users.items():
            times_worked = self.processing_time_punches(key)
            temp_data = {'id': key,
                         'email': value['email'],
                         'firstName': value['firstName'],
                         'lastName': value['lastName'],
                         'photo': value['photo'],
                         'worked_hours': times_worked['total_hours'],
                         'over_time': times_worked['overtime'],
                        }
            result.append(temp_data)

        return result



