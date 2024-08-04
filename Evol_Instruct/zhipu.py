import openai
import time
from zhipuai import ZhipuAI

client = ZhipuAI(api_key='21484fc09011e9eb51fb9a6faf1b7a2d.06mUJgqwhmHlOuzq')

# openai.api_key = 'your api key'
def get_zhipu_compeletion(prompt):
    try:
        response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            stream=True,
            )
        return response
    except Exception as e:
        print(f"Error {e}")
        return None
    

def get_oai_completion(prompt):

    try: 
        response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
       
    ],
   temperature=1,
   max_tokens=2048,
   top_p=0.95,
   frequency_penalty=0,
   presence_penalty=0,
   stop=None
)
        res = response["choices"][0]["message"]["content"]
       
        gpt_output = res
        return gpt_output
    except requests.exceptions.Timeout:
        # Handle the timeout error here
        print("The OpenAI API request timed out. Please try again later.")
        return None
    except openai.error.InvalidRequestError as e:
        # Handle the invalid request error here
        print(f"The OpenAI API request was invalid: {e}")
        return None
    except openai.error.APIError as e:
        if "The operation was timeout" in str(e):
            # Handle the timeout error here
            print("The OpenAI API request timed out. Please try again later.")
#             time.sleep(3)
            return get_oai_completion(prompt)            
        else:
            # Handle other API errors here
            print(f"The OpenAI API returned an error: {e}")
            return None
    except openai.error.RateLimitError as e:
        return get_oai_completion(prompt)

def call_chatgpt(ins):
    success = False
    re_try_count = 15
    ans = ''
    while not success and re_try_count >= 0:
        re_try_count -= 1
        try:
            ans = get_oai_completion(ins)
            success = True
        except:
            time.sleep(5)
            print('retry for sample:', ins)
    return ans