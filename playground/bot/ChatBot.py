import os
import openai


class Bot:
    def __init__(self, name, ai_name = "AI", access = False, personality = "", scenario = "", age = 0) -> None:
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.personality = personality
        self.scenario = scenario
        self.age = age
        self.chat_log = ""
        self.user_name = name
        self.ai_name = ai_name
        self.access = access
        
        self.param={"model" : "text-davinci-003",
                    "temperature" : 0.7,
                    "max_tokens" : 100,
                    "top_p" : 1,
                    "frequency_penalty" :1,
                    "presence_penalty":2}
    

    def response(self, question) -> str:
        self.chat_log += f"{self.user_name}: {question}\n"
        prompt = f"{self.scenario}\n{self.personality}\n{self.chat_log}{self.ai_name}:"
        
        if self.access:
            completion = openai.Completion.create(
                model=self.param["model"],
                prompt=prompt,
                temperature=self.param["temperature"],
                max_tokens=self.param["max_tokens"],
                top_p=self.param["top_p"],
                frequency_penalty=self.param["frequency_penalty"],
                presence_penalty=self.param["presence_penalty"],
                stop = f"\n{self.user_name}: ")
            text = completion.choices[0].text
        else:
            text = f"Echo: {question}"
        
        self.chat_log += f"{self.ai_name}: {text}\n"
        return text
    
            
    def __str__(self):
        return self.chat_log


    def get_param(self):
        for k, v in self.param.items(): 
            print(k, "= ", v)
    

    def set_param(self, **kwargs):
        for key, value in kwargs.items():
            self.param[key] = value
    

    def set_engine(self, engine):
        self.param["model"] = engine