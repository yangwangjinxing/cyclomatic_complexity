U32 find (string match){
       for(auto var : list)
       {
           if(var == match && from != INVALID_U32) return INVALID_U32;
       }
       //match step1
       if(session == getName() && key == getKey())
       {
           for (auto& kv : Map)
           {
               if (kv.second == last && match == kv.first)
               {
                   return last;
               }
           }

       }
       //match step2
       auto var = Map.find(match);
       if(var != Map.end()&& (from != var->second)) return var->second;

       //match step3
       for(auto var: Map)
       {
           if((var.first, match) && from != var.second)
           {
               return var.second;
           }
       }
       return INVALID_U32;
   };
