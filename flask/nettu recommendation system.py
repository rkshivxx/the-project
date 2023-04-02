
import pickle
import pandas as pd


class thalaivar():
    def rec(name,N):
        df = pd.read_csv("C:/Users/rkshi/Downloads/flask/netuflix.csv")
        
        
        
        
        
        
        
        
        data = df[['show_id', 'type', 'title', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']]
        
        
        
        
        data = data.fillna('')
        
        
        
        
        
        
        
        
        
        data['type']=data['type'].apply(lambda x:x.split())
        data['director'] = data['director'].apply(lambda x:x.split(","))
        data['cast'] = data['cast'].apply(lambda x:x.split(","))
        data['country']=data['country'].apply(lambda x:x.split(","))
        data['rating']=data['rating'].apply(lambda x:x.split())
        data['listed_in'] = data['listed_in'].apply(lambda x:x.split(","))
        data['description']=data['description'].apply(lambda x:x.split())
        
        
        
        
        
        data.head()
        
        
        
        
        
        col=['type', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']
        for i in col:
            data[i]=data[i].apply(lambda x:[i.replace(" ","") for i in x])
        
        
        
        
        data['combined_feature']=data['type']+data['director']+data['cast']+data['country']+data['rating']+data['listed_in']+data['description']
        movie = data[['show_id', 'title', 'combined_feature']]
        
        
        
        movie['combined_feature'] = movie['combined_feature'].apply(lambda x:' '.join(x))
        
        
        
        
        
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import linear_kernel
        vectorizer=TfidfVectorizer(stop_words='english')
        response=vectorizer.fit_transform(movie['combined_feature'])
        cosine_similarities = linear_kernel(response,response)
        
        
        
        
        #def rec(name,N):
        top_movies=[]
        ind=movie[movie['title']==name].index[0]
        sim_scores=cosine_similarities[ind]
        sim_scores=sorted((list(enumerate(sim_scores))),reverse=True, key=lambda x:x[1])[1:N+1]
            
        for i in range(len(sim_scores)):
                top_movies+=[(movie['title'][sim_scores[i][0]], sim_scores[i][1])]
          
        return top_movies
            
        
        
            
          
        
        
pi=thalaivar()


with open('model.pkl', 'wb') as f:
    pickle.dump(pi, f)
    
    
    
    
    
    
