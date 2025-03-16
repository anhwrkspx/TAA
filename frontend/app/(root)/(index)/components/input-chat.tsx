import React, { useState } from 'react'
import { Send } from 'lucide-react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import chatAction from '@/lib/actions/chat-action'

interface InputChatProps {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  onChangeMess: (e: any) => void
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  onChangeResult: (e: any) => void
}

const InputChat = ({ onChangeMess, onChangeResult }: InputChatProps) => {
  const [value, setVal] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async () => {
    if (!value.trim()) return;
    
    try {
        onChangeMess((prev:string[]) => [...prev, value]);
        
        setIsLoading(true);
        const data = await chatAction({
            prompt: value,
        });
        
        onChangeResult((prev:string[]) => [...prev, data.result]);
        
        setVal("");
    } catch (error) {
        console.error("Error fetching result:", error);
        onChangeResult((prev:string[]) => [...prev, "Sorry, something went wrong."]);
    } finally {
        setIsLoading(false);
    }
  }
  return (
    <section className='flex gap-2 container mx-auto my-3'>
      <Input
        type='text'
        minLength={10}
        maxLength={1000}
        value={value}
        onChange={(e) => setVal(e.target.value)}
        placeholder="Bạn muốn hỏi gì ?"
        disabled={isLoading}
      />
      <Button 
        onClick={handleSubmit}
        disabled={isLoading || !value.trim()}
      >
        <Send />
      </Button>
    </section>
  )
}

export default InputChat