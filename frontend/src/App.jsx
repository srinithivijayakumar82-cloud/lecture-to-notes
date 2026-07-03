import {useState} from 'react';
function TranscriptInput(){
  const [transcript, setTranscript]=useState('');
  const [result, setResult]=useState('');
  async function backendCall(){
    const response=await fetch('http://127.0.0.1:8000/generate_notes_endpoint',{
      method:'POST',
      headers:{
        'Content-Type':'application/json'
      },
      body:JSON.stringify({
        transcript: transcript
      })
    })
    const data=await response.json();
    setResult(data);
  }
  return(
    <>
      <textarea value={transcript} onChange={(e)=>setTranscript(e.target.value)}/>
      <button onClick={backendCall}>Generate Notes</button>
      {result && (
      <div>
        <h2>{result.title}</h2>
        <p>{result.summary}</p>
        <ul>
          {result.key_points.map((point, index) => (
          <li key={index}>{point}</li>
          ))}
        </ul>
      </div>
    )}
    </>
  )
}

export default TranscriptInput;