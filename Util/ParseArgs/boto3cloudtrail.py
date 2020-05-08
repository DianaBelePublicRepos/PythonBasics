import boto3
import datetime as dt
import argparse


""" Initialising variables with default values """
attribute_key = "default_string"
attribute_value = "default_string"
end_time_of_search  = dt.datetime.now()
parser = argparse.ArgumentParser()
max_number_of_results = 1
profile_name = "default"
start_time_of_search = dt.datetime.now() - dt.timedelta(days = 1)

def define_script_parameters():
    """ Definition of parameters, both mandatory and optional """
    parser.add_argument("profile_name", help = "Name of the aws profile to be used")
    parser.add_argument("max_number_of_results", type = int, help = "Maximum number of results that are to be displayed")
    parser.add_argument("attribute_key",
                        choices = ["EventId", "EventName", "ReadOnly", "Username", "ResourceType", "ResourceName",
                                 "EventSource", "AccessKeyId"],
                        help    = "CloudTrail attribute key for the search. Possible options are EventId | EventName | ReadOnly | Username | ResourceType | ResourceName | EventSource | AccessKeyId ")
    parser.add_argument("attribute_value", help = "Value of the selected CloudTrail attribute key")
    parser.add_argument("-st", "--starttime",
                        help = "Start time of the search in `31/08/20 16:30` format - default set to -1 day")
    parser.add_argument("-et", "--endtime",
                        help = "End time of the search in `31/08/20 16:30` format - default current time")

define_script_parameters()


""" Parsing the list of arguments to get user inputted values """
args                  = parser.parse_args()
attribute_key         = args.attribute_key
attribute_value       = args.attribute_value
max_number_of_results = args.max_number_of_results
profile_name          = args.profile_name


if args.starttime:
    start_time_of_search = args.starttime
    start_stripped_date  = dt.datetime.strptime(start_time_of_search.strip(), "%d/%m/%y %H:%M")

if args.endtime:
    end_time_of_search = args.endtime
    end_stripped_date  = dt.datetime.strptime(end_time_of_search.strip(), "%d/%m/%y %H:%M")


""" Create a boto3 session for the profile_name parameter """
session = boto3.Session(profile_name = profile_name)
cloudtrail = boto3.client('cloudtrail')


def get_events_for_attribute(starttime, endtime, maxnumberofresults, attributekey, attributevalue):
    """ Populating the boto3 client request with the collected values """
    try:
        response = cloudtrail.lookup_events(
            LookupAttributes = [
                {
                    'AttributeKey': attributekey,
                    'AttributeValue': attributevalue
                },
            ],
            StartTime        = starttime,
            EndTime          = endtime,
            MaxResults       = maxnumberofresults
        )
    except Exception as e:
        print(e)
        print('Unable to retrieve CloudTrail events for  "{}"'.format(attributevalue))
        raise(e)
    return response


""" Requesting the events and printing them """
events = get_events_for_attribute(start_time_of_search, end_time_of_search, max_number_of_results, attribute_key, attribute_value)
print(events) 