# import base64, json, sys, base64, time, requests

# 
# 	  Example:
# 	 {
# 	     "url": "https://cms.api.brightcove.com/v1/accounts/57838016001/video",
# 	     "requestType": "PATCH",
# 	     "client_id": "0072bebf-0616-442c-84de-7215bb176061",
# 	     "client_secret": "7M0vMete8vP_Dmb9oIRdUN1S5lrqTvgtVvdfsasd",
# 	     "requestBody": "{\"description\":\"Updated video description\"}"
# 	 }
# Updating an individual video
# 	PATCH  /v1/accounts/{account_id}/videos/{video_id}

# "custom_fields": {
# "property1": "string",
# "property2": "string"
# },

###############################################################################################


# case "updateVideo":
#         var currentVideo = videoData[callNumber];
#         if (isDefined(currentVideo)) {
#           options.url =
#             "https://cms.api.brightcove.com/v1/accounts/" +
#             options.account_id +
#             "/videos/" +
#             currentVideo.id;
#           requestBody = currentVideo;
#           // request body must not contain the video id
#           delete requestBody.id;
#           options.requestBody = JSON.stringify(requestBody);
#           options.requestType = "PATCH";
#           // display the request URL and body
#           apiRequest_field.textContent = options.url;
#           apiRequestBody.textContent = JSON.stringify(requestBody, null, "  ");
#           makeRequest(options, function(response) {
#             responseParsed = JSON.parse(response);
#             response_display.textContent = JSON.stringify(
#               responseParsed,
#               null,
#               "  "
#             );
#             callNumber++;
#             if (callNumber < totalVideos) {
#               setRequest("updateVideo");
#             }
#           });
#         }
#         break;


#f= open("guru99.txt","w+")
# my_list = []
# file1 = open("ClipboardTest.txt","r") 
# for num in file1:
#     my_list.append(num.rstrip())

# # print(my_list)
# file2 = open("cliptest.txt", "w")
# # file2.write(my_list)
# for ml in my_list:
    
#     if count % 10 == 0:
#         file2.write(ml + "\n")
#     else:
#         file2.write(ml + " ")


# print(file2)

# file1.close() 
# file2.close() 

import csv

with open("csv.txt") as c_file:
    # c_read = csv.reader(c_file, delimiter=",")

    line_count = 0
    for row in c_file:
        if line_count == 0:
            line_count += 1
            continue
            
        print(row)
            # first_line = []
            # first_line.append(row.split(","))
            # print(first_line)
            # print(f"Column names: {','.join(row) }")
            # print(f"Column names: {first_line[0]}, {first_line[1]}, {first_line[2]}")
            # line_count +=1
        # else:
        #     print(f"\tIndex: {row[0]}.  Height: {row[1]}. Weight: {row[2]}")
        #     line_count +=1
    print(f"line count: {line_count}")        