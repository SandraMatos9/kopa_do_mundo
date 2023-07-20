import datetime
from rest_framework.views import APIView, Request, Response, status
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError

from utils import data_processing
from .models import Team
from django.forms.models import model_to_dict

class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams= Team.objects.all()

        team_list= []
        for team in teams:
            team_dict= model_to_dict(team)
            team_list.append(team_dict)
        return Response(team_list,status.HTTP_200_OK)
    



    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)

            team = Team.objects.create(**request.data)
            team_dict= model_to_dict(team)
           
            return Response(team_dict,status.HTTP_201_CREATED)
        
        except InvalidYearCupError as err:
            return Response({"error": err.message},status.HTTP_400_BAD_REQUEST)  #"error": "there was no world cup this year"
        except NegativeTitlesError as err:
            return Response({"error": err.message},status.HTTP_400_BAD_REQUEST)  # "error": "titles cannot be negative"
        except ImpossibleTitlesError as err:
            return Response({"error": err.message},status.HTTP_400_BAD_REQUEST) #"impossible to have more titles than disputed cups"
         
        
class TeamDetails(APIView):
    def get(self,request:Request, team_id: int) -> Response:
       
        try:
            team = Team.objects.get(id = team_id)
            team_dict= model_to_dict(team) 
            return Response(team_dict, status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND) 
        


    def patch(self,request:Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        for key,value in request.data.items():
            setattr(team, key, value)
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict,status.HTTP_200_OK)    
        
    def delete(self,request:Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


    
     
   

    


        

# Create your views here.
